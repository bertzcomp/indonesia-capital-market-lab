import json

# Ganti 'data_saham.json' dengan path file JSON Anda
with open('/Users/albert/Documents/Finances/data/raw/market_data/allCompanies.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# List untuk menampung hasil ekstraksi
extracted_data = []

# Iterasi setiap saham
for item in data.get('data', []):
    # Pastikan hanya saham (EfekEmiten_Saham = True)
    if item.get('EfekEmiten_Saham', False):
        extracted_data.append({
            "Industri": item.get("Industri", ""),
            "SubIndustri": item.get("SubIndustri", ""),
            "KodeEmiten": item.get("KodeEmiten", ""),
            "Sektor": item.get("Sektor", ""),
            "SubSektor": item.get("SubSektor", "")
        })

# Simpan hasil ke file baru
with open('/Users/albert/Documents/Finances/data/processed/stocks_sectors.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=2)

print("Ekstraksi selesai! Hasil tersimpan di 'hasil_ekstraksi.json'.")