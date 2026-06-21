from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import UserAlreadyParticipantError
import os
import csv
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def join_private_channel(invite_link):
    try:
        hash_part = invite_link.split("/")[-1].replace("+", "")
        await client(ImportChatInviteRequest(hash_part))
        print(f"✅ Joined private channel: {invite_link}")
    except UserAlreadyParticipantError:
        print(f"⚠️ Already joined private channel: {invite_link}, lanjut scrape...")
    except Exception as e:
        print(f"❌ Failed to join private channel: {e}")

async def scrape_last_n_days(channel, csv_filename, days=4):
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)

    os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

    rows = []
    async for message in client.iter_messages(channel):
        if message.date < cutoff_date:
            break

        rows.append([
            message.date,
            message.sender_id,
            message.sender.username if message.sender else None,
            message.text
        ])

    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "sender_id", "username", "message"])
        writer.writerows(rows)

    print(f"✅ Scraping selesai. {len(rows)} pesan disimpan di {csv_filename}")

async def main():
    invite_link = "https://t.me/+9PzppSYAs4E3OGQ1"

    channel_name = invite_link.split("/")[-1].replace("+","")
    filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/telegram/data/TKSI/{channel_name}_messages_20260128_20260131.csv"

    await join_private_channel(invite_link)
    await scrape_last_n_days(invite_link, filename, days=90)


with client:
    client.loop.run_until_complete(main())
