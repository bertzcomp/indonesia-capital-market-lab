from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os
import csv
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Load env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def join_channel(channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"Joined channel {channel_link}")
    except:
        print("Already joined or failed")


async def scrape_last_3_days(channel, csv_filename):
    three_days_ago = datetime.now(timezone.utc) - timedelta(days=4)

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "sender_id", "username", "message"])

        async for message in client.iter_messages(channel):
            if message.date < three_days_ago:
                break

            writer.writerow([
                message.date,
                message.sender_id,
                message.sender.username if message.sender else None,
                message.text
            ])

    print(f"Scraping selesai. Data disimpan di {csv_filename}")

async def main():
    channel_link = "https://t.me/stockswingerbyy"
    channel_name = channel_link.split("/")[-1]
    filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/telegram/data/SS/{channel_name}_messages_20260128_20260131.csv" ## replace x_days

    await join_channel(channel_link)
    await scrape_last_3_days(channel_link, filename)

with client:
    client.loop.run_until_complete(main())
