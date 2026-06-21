import json
import logging
import os
import tempfile
import time

import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from utils.logger_config import logger

# Suppress noisy logs
for _name in (
    "selenium",
    "selenium.webdriver",
    "selenium.webdriver.remote.remote_connection",
    "urllib3",
):
    logging.getLogger(_name).setLevel(logging.WARNING)


class StockbitTokenFetcher:
    def __init__(self):
        self.login_url = "https://stockbit.com/login"

        profile_dir = os.path.join(
            os.path.expanduser("~"), ".idx-fundamental-stockbit-profile"
        )
        os.makedirs(profile_dir, exist_ok=True)

        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={profile_dir}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Enable performance logging
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        logger.info("Launching undetected ChromeDriver...")

        # IMPORTANT: Match Chrome version (you are on 146)
        self.driver = uc.Chrome(
            options=options,
            headless=False,
            use_subprocess=True,
            version_main=148
        )

        tmp_dir = tempfile.gettempdir()
        self.token_path = os.path.join(tmp_dir, "stockbit_token.tmp")

    def fetch_tokens(self):
        driver = self.driver

        logger.info("Opening Stockbit login page...")
        driver.get(self.login_url)

        logger.info("Please log in manually in the opened browser.")
        input("Press Enter AFTER login and dashboard fully loaded... ")

        # Wait network calls
        time.sleep(5)

        logger.info("Capturing network logs for Authorization token...")

        logs = driver.get_log("performance")
        access_token = None

        for entry in logs:
            try:
                message = json.loads(entry["message"])
                method = message.get("message", {}).get("method")

                if method == "Network.requestWillBeSent":
                    params = message["message"]["params"]
                    request = params.get("request", {})
                    url = request.get("url", "")

                    # Capture ANY request to exodus.stockbit.com
                    if "exodus.stockbit.com" in url:
                        headers = request.get("headers", {})
                        auth_header = headers.get("Authorization") or headers.get("authorization")

                        if auth_header and auth_header.startswith("Bearer "):
                            access_token = auth_header.split(" ", 1)[1]
                            logger.info(f"Token captured from URL: {url}")
                            break

            except Exception:
                continue

        if not access_token:
            logger.error("Failed to capture Bearer token from network logs.")
            return None

        logger.info("Access token captured successfully.")

        with open(self.token_path, "w") as f:
            f.write(access_token)

        logger.info(f"Token saved to: {self.token_path}")

        return access_token

    def load_token(self):
        if os.path.exists(self.token_path):
            with open(self.token_path, "r") as f:
                return f.read().strip()
        return None

    def close(self):
        try:
            self.driver.quit()
        except Exception:
            pass