"""
IDX Disclosure Scraper - API-based
Mengambil pengumuman dari endpoint GetAnnouncement IDX secara langsung.

Author: Albert (refactored)
Strategy: Panggil JSON API langsung, bukan scrape DOM

"""

import os
import re
import csv
import json
import time
import logging
import requests
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urlencode

# ─── Logging ────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("idx_api_scraper.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ─── Konstanta ───────────────────────────────────────────────────────────────

BASE_URL = "https://www.idx.co.id"
API_URL  = f"{BASE_URL}/primary/ListedCompany/GetAnnouncement"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.idx.co.id/id/perusahaan-tercatat/keterbukaan-informasi/",
    "Origin": "https://www.idx.co.id",
    "X-Requested-With": "XMLHttpRequest",
}

PAGE_SIZE = 50  # Bisa sampai 100, tapi 50 lebih aman


# ─── Helper ──────────────────────────────────────────────────────────────────

def clean_kode(kode: str) -> str:
    """Trim whitespace dari kode emiten IDX (field-nya dipadding spasi)."""
    return kode.strip() if kode else ""


def safe_filename(name: str, max_len: int = 180) -> str:
    """Buat nama file yang aman dari string apapun."""
    name = re.sub(r'[\\/:*?"<>|]', "_", name)
    return name[:max_len]


def build_session() -> requests.Session:
    """
    Buat requests.Session dengan headers mirip browser.
    Coba ambil cookie dari idx.co.id terlebih dahulu agar tidak 403.
    """
    s = requests.Session()
    s.headers.update(DEFAULT_HEADERS)

    log.info("Mengambil cookie dari homepage IDX...")
    try:
        r = s.get(f"{BASE_URL}/id/perusahaan-tercatat/keterbukaan-informasi/", timeout=20)
        r.raise_for_status()
        log.info(f"Cookie berhasil: {dict(s.cookies)}")
    except Exception as e:
        log.warning(f"Gagal ambil cookie awal: {e} — lanjut tanpa cookie")

    return s


# ─── Core Scraper ────────────────────────────────────────────────────────────

def fetch_page(session: requests.Session, params: dict, retries: int = 3) -> dict | None:
    """
    Panggil satu halaman API GetAnnouncement.
    Return dict JSON atau None jika gagal.
    """
    for attempt in range(1, retries + 1):
        try:
            resp = session.get(API_URL, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            else:
                log.warning(f"HTTP {resp.status_code} pada percobaan {attempt}")
        except requests.RequestException as e:
            log.warning(f"Request error percobaan {attempt}: {e}")

        if attempt < retries:
            sleep_sec = 2 ** attempt  # exponential backoff
            log.info(f"Tunggu {sleep_sec}s sebelum retry...")
            time.sleep(sleep_sec)

    return None


def parse_reply(reply: dict, page_index: int) -> list[dict]:
    """
    Ubah satu entry 'Replies' dari API menjadi list baris CSV.
    Satu entry bisa menghasilkan beberapa baris (satu per attachment).
    """
    ann = reply.get("pengumuman", {})
    attachments = reply.get("attachments", [])

    kode_emiten   = clean_kode(ann.get("Kode_Emiten", ""))
    no_pengumuman = ann.get("NoPengumuman", "")
    judul         = ann.get("JudulPengumuman", "")
    perihal       = ann.get("PerihalPengumuman", "")
    tgl_raw       = ann.get("TglPengumuman", "")
    jenis         = ann.get("JenisPengumuman", "")
    form_id       = ann.get("Form_Id", "")

    # Parse tanggal
    tanggal = ""
    waktu   = ""
    if tgl_raw:
        try:
            dt = datetime.fromisoformat(tgl_raw)
            tanggal = dt.strftime("%Y-%m-%d")
            waktu   = dt.strftime("%H:%M:%S")
        except ValueError:
            tanggal = tgl_raw[:10]

    rows = []

    if not attachments:
        # Pengumuman tanpa lampiran — tetap simpan satu baris
        rows.append({
            "HalamanAPI"    : page_index,
            "KodeEmiten"    : kode_emiten,
            "NoPengumuman"  : no_pengumuman,
            "Tanggal"       : tanggal,
            "Waktu"         : waktu,
            "Judul"         : judul,
            "Perihal"       : perihal,
            "JenisPengumuman": jenis,
            "FormId"        : form_id,
            "IsLampiran"    : False,
            "NamaFile"      : "",
            "LinkPDF"       : "",
        })
    else:
        for att in attachments:
            full_path      = att.get("FullSavePath", "")
            original_name  = att.get("OriginalFilename", "")
            is_attachment  = att.get("IsAttachment", False)

            rows.append({
                "HalamanAPI"    : page_index,
                "KodeEmiten"    : kode_emiten,
                "NoPengumuman"  : no_pengumuman,
                "Tanggal"       : tanggal,
                "Waktu"         : waktu,
                "Judul"         : judul,
                "Perihal"       : perihal,
                "JenisPengumuman": jenis,
                "FormId"        : form_id,
                "IsLampiran"    : is_attachment,
                "NamaFile"      : original_name,
                "LinkPDF"       : full_path,
            })

    return rows


def scrape_all(
    session       : requests.Session,
    keyword       : str   = "",
    kode_emiten   : str   = "",
    date_from     : str   = "19010101",
    date_to       : str   = "",
    emiten_type   : str   = "s",
    lang          : str   = "id",
    max_records   : int   = 0,          # 0 = ambil semua
    delay_sec     : float = 1.0,
) -> list[dict]:
    """
    Ambil semua halaman dari GetAnnouncement API.
    """
    if not date_to:
        date_to = datetime.today().strftime("%Y%m%d")

    all_rows     = []
    index_from   = 0
    total_avail  = None
    page_num     = 0

    while True:
        page_num += 1
        params = {
            "kodeEmiten" : kode_emiten,
            "emitenType" : emiten_type,
            "indexFrom"  : index_from,
            "pageSize"   : PAGE_SIZE,
            "dateFrom"   : date_from,
            "dateTo"     : date_to,
            "lang"       : lang,
            "keyword"    : keyword,
        }

        log.info(f"[Page {page_num}] indexFrom={index_from}, keyword='{keyword}'")
        data = fetch_page(session, params)

        if data is None:
            log.error("Gagal fetch halaman, berhenti.")
            break

        if total_avail is None:
            total_avail = data.get("ResultCount", 0)
            log.info(f"Total records tersedia: {total_avail}")

        replies = data.get("Replies", [])
        if not replies:
            log.info("Tidak ada reply lagi, scraping selesai.")
            break

        for reply in replies:
            all_rows.extend(parse_reply(reply, page_num))

        fetched_so_far = index_from + len(replies)
        log.info(f"  → {len(replies)} pengumuman, total terkumpul: {fetched_so_far}/{total_avail}")

        # Cek apakah sudah semua
        if fetched_so_far >= total_avail:
            log.info("Semua data sudah diambil.")
            break

        # Cek limit max_records
        if max_records > 0 and fetched_so_far >= max_records:
            log.info(f"Mencapai batas max_records={max_records}, berhenti.")
            break

        index_from += PAGE_SIZE
        time.sleep(delay_sec)

    return all_rows


# ─── CSV Export ──────────────────────────────────────────────────────────────

FIELDNAMES = [
    "HalamanAPI", "KodeEmiten", "NoPengumuman", "Tanggal", "Waktu",
    "Judul", "Perihal", "JenisPengumuman", "FormId",
    "IsLampiran", "NamaFile", "LinkPDF",
]


def save_csv(rows: list[dict], path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"✅ CSV disimpan: {path} ({len(rows)} baris)")


# ─── PDF Downloader ──────────────────────────────────────────────────────────

def download_pdfs(
    rows        : list[dict],
    save_dir    : str   = "pdf_idx",
    delay_sec   : float = 1.5,
    max_files   : int   = 0,        # 0 = semua
    skip_lampiran: bool = False,    # True = hanya dokumen utama (IsLampiran=False)
) -> None:
    """
    Download PDF dari kolom LinkPDF.
    Gunakan session yang sama agar cookie tetap valid.
    """
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)

    session = build_session()

    # Filter baris yang punya link PDF
    to_download = [r for r in rows if r.get("LinkPDF", "").endswith(".pdf")]

    if skip_lampiran:
        to_download = [r for r in to_download if not r.get("IsLampiran", False)]

    if max_files > 0:
        to_download = to_download[:max_files]

    total = len(to_download)
    log.info(f"📥 Akan download {total} file PDF ke '{save_dir}'")

    success = 0
    fail    = 0

    for i, row in enumerate(to_download, 1):
        url       = row["LinkPDF"]
        nama_file = row.get("NamaFile", "")
        kode      = row.get("KodeEmiten", "unknown")
        tanggal   = row.get("Tanggal", "").replace("-", "")

        # Tentukan nama file lokal
        if nama_file:
            local_name = safe_filename(nama_file)
            if not local_name.endswith(".pdf"):
                local_name += ".pdf"
        else:
            # Fallback dari URL
            url_basename = url.split("/")[-1]
            local_name   = f"{kode}_{tanggal}_{url_basename}"

        dest = save_path / local_name

        # Skip jika sudah ada
        if dest.exists():
            log.info(f"[{i}/{total}] SKIP (sudah ada): {local_name}")
            success += 1
            continue

        log.info(f"[{i}/{total}] Download: {local_name}")
        try:
            resp = session.get(url, timeout=40, stream=True)
            if resp.ok:
                with open(dest, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=8192):
                        f.write(chunk)
                log.info(f"   ✅ OK ({dest.stat().st_size // 1024} KB)")
                success += 1
            else:
                log.warning(f"   ❌ HTTP {resp.status_code}")
                fail += 1
        except Exception as e:
            log.warning(f"   ❌ Error: {e}")
            fail += 1

        if i < total:
            time.sleep(delay_sec)

    log.info(f"\n📊 Download selesai: {success} berhasil, {fail} gagal")
    log.info(f"💾 File disimpan di: {save_path.absolute()}")


# ─── CLI Entry Point ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="IDX Disclosure Scraper — API-based"
    )
    parser.add_argument("--keyword",      default="",         help="Kata kunci pencarian (contoh: volati)")
    parser.add_argument("--kode",         default="",         help="Kode emiten (kosong = semua)")
    parser.add_argument("--date-from",    default="20260101", help="Tanggal mulai YYYYMMDD")
    parser.add_argument("--date-to",      default="",         help="Tanggal akhir YYYYMMDD (default: hari ini)")
    parser.add_argument("--lang",         default="id",       help="Bahasa: id / en")
    parser.add_argument("--max-records",  default=0,  type=int, help="Batas jumlah pengumuman (0=semua)")
    parser.add_argument("--delay",        default=1.0, type=float, help="Delay antar request (detik)")
    parser.add_argument("--output-dir",   default="data",     help="Direktori output CSV")
    parser.add_argument("--download-pdf", action="store_true", help="Download semua PDF setelah scrape")
    parser.add_argument("--pdf-dir",      default="pdf_idx",  help="Direktori simpan PDF")
    parser.add_argument("--max-pdf",      default=0, type=int, help="Batas jumlah PDF didownload (0=semua)")
    parser.add_argument("--only-main",    action="store_true", help="Hanya download dokumen utama (bukan lampiran)")
    args = parser.parse_args()

    print("=" * 65)
    print("  IDX DISCLOSURE SCRAPER — API Mode")
    print("=" * 65)

    session = build_session()

    rows = scrape_all(
        session     = session,
        keyword     = args.keyword,
        kode_emiten = args.kode,
        date_from   = args.date_from,
        date_to     = args.date_to,
        lang        = args.lang,
        max_records = args.max_records,
        delay_sec   = args.delay,
    )

    if not rows:
        print("\n❌ Tidak ada data ditemukan.")
        return

    # Simpan CSV
    ts         = datetime.now().strftime("%Y%m%d_%H%M%S")
    keyword_tag = f"_{args.keyword}" if args.keyword else ""
    csv_path   = f"{args.output_dir}/idx_disclosures{keyword_tag}_{ts}.csv"
    save_csv(rows, csv_path)

    # Summary
    unique_emiten = len({r["KodeEmiten"] for r in rows if r["KodeEmiten"]})
    print(f"\n📊 RINGKASAN:")
    print(f"   Total baris  : {len(rows)}")
    print(f"   Emiten unik  : {unique_emiten}")
    print(f"   CSV          : {csv_path}")

    # Download PDF opsional
    if args.download_pdf:
        print(f"\n📥 Memulai download PDF...")
        download_pdfs(
            rows         = rows,
            save_dir     = args.pdf_dir,
            delay_sec    = args.delay,
            max_files    = args.max_pdf,
            skip_lampiran= args.only_main,
        )

    print("\n✅ Selesai!")


if __name__ == "__main__":
    main()