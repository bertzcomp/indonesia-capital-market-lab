from datetime import datetime, timezone
from dotenv import load_dotenv

from schemas.fundamental import (
    Fundamental,
    PerShare,
    Solvency,
    ManagementEffectiveness,
    Profitability,
    Growth,
    Dividend,
    MarketRank,
    IncomeStatement,
    BalanceSheet,
    CashFlowStatement,
    PricePerformance,
    CurrentValuation,
    Stat,
)
from schemas.sentiment import Sentiment
from schemas.stock import Stock
from schemas.stock_price import StockPrice
from services.stockbit_api_client import StockbitApiClient
from utils.helpers import (
    parse_currency_to_float,
    parse_key_statistic_results_item_value,
)
from utils.logger_config import logger
from typing import Iterator, List, Dict, Optional
import re
import time

load_dotenv()


class StockBit:
    """
    A class to interact with the StockBit API and fetch key statistics, stock price, and sentiment for stocks.
    """

    def __init__(self, stocks: [Stock]):
        """
        Initializes the StockBit provider with necessary headers and URL.
        """
        logger.info("StockBit provider initialised")
        self.stocks = stocks
        self.base_url = "https://exodus.stockbit.com"
        self.key_statistic = None
        self.stockbit_api_client = StockbitApiClient()

    def key_statistic_by_stock(self, stock: Stock) -> dict:
        """
        Retrieves key statistics for a given stock by sending a GET request to the API.

        Args:
            stock (Stock): An instance of the Stock class containing the ticker symbol.

        Returns:
            dict: A dictionary containing the key statistics if the request is successful.
            None: If the request fails after retrying or encounters an error.

        Raises:
            requests.exceptions.RequestException: If the request fails due to network issues or invalid URL.

        Side Effects:
            - Logs an error message if the response status code is not 200.
            - Re-authenticates if a 401 Unauthorized status code is received and retries the request up to 3 times.
            - Logs an error message if the request fails due to an exception.
            - Logs an informational message if the request fails after all retries.
        """
        url = f"{self.base_url}/keystats/ratio/v1/{stock.ticker}?year_limit=10"

        return self.stockbit_api_client.get(url)

    def with_fundamental(self):
        """
        Get fundamentals for a list of stocks.

        Returns:
            Self
        """
        processed = 1
        for stock in self.stocks:
            logger.info(
                f"Processing key statistic for: {stock.ticker} ({processed}/{len(self.stocks)})"
            )
            self.key_statistic = self.key_statistic_by_stock(stock)

            if self.key_statistic:
                stock.fundamental = self._fundamental(stock)

            time.sleep(0.1)
            logger.debug(stock)
            processed += 1

        return self

    def _fundamental(self, stock: Stock) -> Fundamental | None:
        """
        Parses the API response data and returns a Fundamental object.

        Args:
            stock (Stock): The Stock object for which the fundamental data is being parsed.

        Returns:
            Fundamental: An object containing parsed fundamental data.
        """

        if self.key_statistic == {}:
            return None

        fundamental = Fundamental()
        fundamental.stock = stock

        data = self.key_statistic["data"]

        # Stats
        #
        stat = Stat(
            parse_currency_to_float(data["stats"]["current_share_outstanding"]),
            parse_currency_to_float(data["stats"]["market_cap"]),
            parse_currency_to_float(data["stats"]["enterprise_value"]),
        )
        fundamental.stat = stat
        logger.debug(stat)

        # -- nested object
        closure_fin_items_results = data["closure_fin_items_results"]

        # Current Valuation
        #
        current_valuation_fin_name_results = closure_fin_items_results[0][
            "fin_name_results"
        ]

        current_valuation = CurrentValuation(
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 0
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 1
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 2
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 3
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 4
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 5
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 6
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 7
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 8
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 9
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 10
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 11
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 12
            ),
            parse_key_statistic_results_item_value(
                current_valuation_fin_name_results, 13
            ),
        )
        fundamental.current_valuation = current_valuation
        logger.debug(current_valuation)

        # Per Share
        #
        per_share_fin_name_results = closure_fin_items_results[1]["fin_name_results"]
        per_share = PerShare(
            parse_key_statistic_results_item_value(per_share_fin_name_results, 0),
            parse_key_statistic_results_item_value(per_share_fin_name_results, 1),
            parse_key_statistic_results_item_value(per_share_fin_name_results, 2),
            parse_key_statistic_results_item_value(per_share_fin_name_results, 3),
            parse_key_statistic_results_item_value(per_share_fin_name_results, 4),
            parse_key_statistic_results_item_value(per_share_fin_name_results, 5),
        )
        fundamental.per_share = per_share
        logger.debug(per_share)

        # Solvency
        #
        solvency_fin_name_results = closure_fin_items_results[2]["fin_name_results"]
        solvency = Solvency(
            parse_key_statistic_results_item_value(solvency_fin_name_results, 0),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 1),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 2),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 3),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 4),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 5),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 6),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 7),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 8),
            parse_key_statistic_results_item_value(solvency_fin_name_results, 9),
        )
        fundamental.solvency = solvency
        logger.debug(solvency)

        # Management Effectivieness
        management_effectiveness_fin_name_results = closure_fin_items_results[3][
            "fin_name_results"
        ]
        management_effectiveness = ManagementEffectiveness(
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 0
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 1
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 2
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 3
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 4
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 5
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 6
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 7
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 8
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 9
            ),
            parse_key_statistic_results_item_value(
                management_effectiveness_fin_name_results, 10
            ),
        )
        fundamental.management_effectiveness = management_effectiveness
        logger.debug(management_effectiveness)

        # Profitability
        #
        profitability_fin_name_results = closure_fin_items_results[4][
            "fin_name_results"
        ]
        profitability = Profitability(
            parse_key_statistic_results_item_value(profitability_fin_name_results, 0),
            parse_key_statistic_results_item_value(profitability_fin_name_results, 1),
            parse_key_statistic_results_item_value(profitability_fin_name_results, 2),
        )
        fundamental.profitability = profitability
        logger.debug(profitability)

        # Growth
        #
        growth_fin_name_results = closure_fin_items_results[5]["fin_name_results"]
        growth = Growth(
            parse_key_statistic_results_item_value(growth_fin_name_results, 0),
            parse_key_statistic_results_item_value(growth_fin_name_results, 1),
            parse_key_statistic_results_item_value(growth_fin_name_results, 2),
        )
        fundamental.growth = growth
        logger.debug(growth)

        # Dividend
        #
        dividend_fin_name_results = closure_fin_items_results[6]["fin_name_results"]
        dividend = Dividend(
            parse_key_statistic_results_item_value(dividend_fin_name_results, 0),
            parse_key_statistic_results_item_value(dividend_fin_name_results, 1),
            parse_key_statistic_results_item_value(dividend_fin_name_results, 2),
            parse_key_statistic_results_item_value(dividend_fin_name_results, 3),
            parse_key_statistic_results_item_value(dividend_fin_name_results, 4),
        )
        fundamental.dividend = dividend
        logger.debug(dividend)

        # Market Rank
        #
        market_rank_fin_name_results = closure_fin_items_results[7]["fin_name_results"]
        market_rank = MarketRank(
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 0),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 1),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 2),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 3),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 4),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 5),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 6),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 7),
            parse_key_statistic_results_item_value(market_rank_fin_name_results, 8),
        )
        fundamental.market_rank = market_rank
        logger.debug(market_rank)

        # Income Statement
        #
        income_statement_fin_name_results = closure_fin_items_results[8][
            "fin_name_results"
        ]
        income_statement = IncomeStatement(
            parse_key_statistic_results_item_value(
                income_statement_fin_name_results, 0
            ),
            parse_key_statistic_results_item_value(
                income_statement_fin_name_results, 1
            ),
            parse_key_statistic_results_item_value(
                income_statement_fin_name_results, 2
            ),
            parse_key_statistic_results_item_value(
                income_statement_fin_name_results, 3
            ),
        )
        fundamental.income_statement = income_statement
        logger.debug(income_statement)

        # Balance Sheet
        #
        balance_sheet_fin_name_results = closure_fin_items_results[9][
            "fin_name_results"
        ]
        balance_sheet = BalanceSheet(
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 0),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 1),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 2),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 3),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 4),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 5),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 6),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 7),
            parse_key_statistic_results_item_value(balance_sheet_fin_name_results, 8),
        )
        fundamental.balance_sheet = balance_sheet
        logger.debug(balance_sheet)

        # Cash Flow
        #
        cash_flow_statement_fin_name_results = closure_fin_items_results[10][
            "fin_name_results"
        ]
        cash_flow_statement = CashFlowStatement(
            parse_key_statistic_results_item_value(
                cash_flow_statement_fin_name_results, 0
            ),
            parse_key_statistic_results_item_value(
                cash_flow_statement_fin_name_results, 1
            ),
            parse_key_statistic_results_item_value(
                cash_flow_statement_fin_name_results, 2
            ),
            parse_key_statistic_results_item_value(
                cash_flow_statement_fin_name_results, 3
            ),
            parse_key_statistic_results_item_value(
                cash_flow_statement_fin_name_results, 4
            ),
        )
        fundamental.cash_flow_statement = cash_flow_statement
        logger.debug(cash_flow_statement)

        # Price Performance
        #
        price_performance_fin_name_results = closure_fin_items_results[11][
            "fin_name_results"
        ]
        price_performance = PricePerformance(
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 0
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 1
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 2
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 3
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 4
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 5
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 6
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 7
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 8
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 9
            ),
            parse_key_statistic_results_item_value(
                price_performance_fin_name_results, 10
            ),
        )
        fundamental.price_performance = price_performance

        return fundamental

    def stock_price_by_stock(self, stock: Stock) -> Stock:
        """
        Fetches the stock price data for a given stock.

        This method constructs a URL using the base URL and the stock's ticker symbol,
        then makes an HTTP GET request to retrieve the stock price data associated with that stock.

        Parameters:
        - stock (Stock): An instance of the Stock class containing the ticker symbol
          for which the stock price data is to be fetched.

        Returns:
        - Stock: The stock price data extracted from the response.
        """
        url = (
            f"{self.base_url}/company-price-feed/v2/orderbook/companies/{stock.ticker}"
        )

        return self.stockbit_api_client.get(url)

    def with_stock_price(self):
        """
        Updates each stock in the stocks list with detailed price data.

        This method iterates over each stock in the `stocks` list, fetching the latest stock price data.
        It updates various attributes of the stock with the retrieved data, such as last price, change, volume, etc.
        The method pauses briefly between processing each stock to avoid overwhelming the server with requests.

        Returns:
        - self: The instance of the class, allowing for method chaining.
        """
        processed = 1
        for stock in self.stocks:
            logger.info(
                f"Processing stock price for: {stock.ticker} ({processed}/{len(self.stocks)})"
            )
            response = self.stock_price_by_stock(stock)

            if response == {}:
                logger.warning(
                    f"Skipped to fetch stock price for {stock.ticker} because empty response!"
                )
                continue

            data = response["data"]

            stock.stock_price = StockPrice(
                price=data["lastprice"],
                change=data["change"],
                fbuy=data["fbuy"],
                fsell=data["fsell"],
                volume=data["volume"],
                percentage_change=data["percentage_change"],
                average=data["average"],
                close=data["close"],
                high=data["high"],
                low=data["low"],
                open=data["open"],
                ara=float(data["ara"]["value"].replace(",", "")),
                arb=float(data["arb"]["value"].replace(",", "")),
                frequency=data["frequency"],
            )

            time.sleep(0.1)

            logger.debug(stock)
            processed += 1

        return self

    def stream_pinned_by_stock(self, stock: Stock) -> dict:
        """
        Fetches the pinned stream data for a given stock.

        This method constructs a URL using the base URL and the stock's ticker symbol,
        then makes an HTTP GET request to retrieve the pinned stream data associated
        with that stock.

        Parameters:
        - stock (Stock): An instance of the Stock class containing the ticker symbol
          for which the pinned stream data is to be fetched.

        Returns:
        - dict: A dictionary containing the response data from the HTTP GET request.
        """
        url = f"{self.base_url}/stream/v3/symbol/{stock.ticker}/pinned"

        return self.stockbit_api_client.get(url)

    def stream_by_stock(self, stock: Stock) -> dict:
        """
        Fetches the stream data for a given stock.

        This method constructs a URL using the base URL and the stock's ticker symbol,
        then makes an HTTP POST request to retrieve the stream data associated with that stock.
        The request includes a payload specifying the category, last stream ID, and limit.

        Parameters:
        - stock (Stock): An instance of the Stock class containing the ticker symbol
          for which the stream data is to be fetched.

        Returns:
        - dict: A dictionary containing the response data from the HTTP POST request.
        """
        url = f"{self.base_url}/stream/v3/symbol/{stock.ticker}"
        payload = {"category": "STREAM_CATEGORY_ALL", "last_stream_id": 0, "limit": 20}
        return self.stockbit_api_client.post(url, payload)

    def with_stream_data(self):
        """
        Updates each stock in the stocks list with sentiment data from stream and pinned stream sources.

        This method iterates over each stock in the `stocks` list, fetching both pinned and regular stream data.
        It processes the response to extract sentiment information, which is then added to the stock's sentiment attribute.
        The method pauses briefly between processing each stock to avoid overwhelming the server with requests.

        Returns:
        - self: The instance of the class, allowing for method chaining.
        """
        processed = 1
        for stock in self.stocks:
            logger.info(
                f"Processing stream data for: {stock.ticker} ({processed}/{len(self.stocks)})"
            )
            response_stream_pinned = self.stream_pinned_by_stock(stock)
            response_stream = self.stream_by_stock(stock)

            if response_stream_pinned != {}:
                pinned_data = response_stream_pinned["data"]

                if pinned_data is not None:
                    posted_at = datetime.fromisoformat(pinned_data["created_at"])
                    sentiment = Sentiment(
                        content=pinned_data["content"], posted_at=posted_at
                    )

                    stock.sentiment = [sentiment]

            if response_stream != {}:
                stream_data = response_stream["data"]["stream"]

                if stream_data is not None:
                    for stream in stream_data:
                        posted_at = datetime.fromisoformat(stream["created_at"])

                        sentiment = Sentiment(
                            content=stream["content"], posted_at=posted_at
                        )

                        if stock.sentiment is None:
                            stock.sentiment = [sentiment]
                        else:
                            stock.sentiment.append(sentiment)

            time.sleep(0.1)
            processed += 1
            logger.debug(stock)

        return self


    def get_running_trade_batches(self, 
                                  max_scroll=3, 
                                  delay=0.5, 
                                  debug=True
                                  ):
        """
        Fetch running trades using cursor-based pagination (robust).
        - max_scroll: number of 50-item pages to attempt
        - delay: seconds between requests
        - debug: if True, print debug info (URL, cursor, response summary)
        """
        all_trades = []
        trade_number = None
        previous_trade_number = None

        for scroll in range(max_scroll):
            endpoint = "/order-trade/running-trade?sort=DESC&limit=50&order_by=RUNNING_TRADE_ORDER_BY_TIME"
            if trade_number is not None:
                endpoint += f"&trade_number={trade_number}"

            url = f"{self.base_url}{endpoint}"

            if debug:
                print(f"[RUN] Requesting: {url}")

            # call client - adjust if your client expects endpoint only
            response = self.stockbit_api_client.get(url)

            # defensive: sometimes client returns JSON string
            if isinstance(response, str):
                try:
                    response = json.loads(response)
                except Exception:
                    if debug:
                        print("Response is string and not JSON-decodable.")
                    response = {}

            if debug:
                # print high-level keys and a short preview (avoid printing huge output)
                if isinstance(response, dict):
                    keys = list(response.keys())
                    print(f"[RUN] Response keys: {keys}")
                    # preview first 200 chars of 'running_trade' if present
                    if "running_trade" in response:
                        print(f"[RUN] running_trade length: {len(response.get('running_trade') or [])}")
                    else:
                        # also check nested common structures
                        if "data" in response and isinstance(response["data"], dict) and "running_trade" in response["data"]:
                            print(f"[RUN] nested data.running_trade length: {len(response['data']['running_trade'] or [])}")
                else:
                    print(f"[RUN] Response type: {type(response)}")

            # Extract trades in a robust way
            running_trades = []

            # direct key
            if isinstance(response, dict) and "running_trade" in response:
                running_trades = response.get("running_trade") or []

            # nested under 'data'
            elif isinstance(response, dict) and "data" in response:
                data = response.get("data")
                if isinstance(data, dict) and "running_trade" in data:
                    running_trades = data.get("running_trade") or []
                elif isinstance(data, list):
                    # sometimes 'data' IS the list
                    running_trades = data

            # final fallback: if top-level is a list
            elif isinstance(response, list):
                running_trades = response

            # If still empty, try alternative keys
            if not running_trades and isinstance(response, dict):
                # try some other plausible keys
                for k in ("items", "results", "rows", "trades"):
                    candidate = response.get(k)
                    if candidate:
                        running_trades = candidate
                        if debug:
                            print(f"[RUN] Found trades under key '{k}' (len={len(running_trades)})")
                        break

            # If still empty, attempt one retry with trade_number-1 (exclusive cursor)
            if not running_trades and trade_number is not None:
                try:
                    tn_minus = int(str(trade_number).replace(",", "")) - 1
                except Exception:
                    tn_minus = None

                # avoid retrying same tn_minus more than once
                if tn_minus and tn_minus != previous_trade_number:
                    if debug:
                        print(f"[RUN] No trades returned for trade_number={trade_number}. Trying trade_number={tn_minus} as fallback...")
                    endpoint2 = f"/order-trade/running-trade?sort=DESC&limit=50&order_by=RUNNING_TRADE_ORDER_BY_TIME&trade_number={tn_minus}"
                    url2 = f"{self.base_url}{endpoint2}"
                    if debug:
                        print(f"[RUN] Retry Requesting: {url2}")
                    response2 = self.stockbit_api_client.get(url2)

                    if isinstance(response2, str):
                        try:
                            response2 = json.loads(response2)
                        except Exception:
                            response2 = {}

                    # try to pull running_trade from retry response
                    if isinstance(response2, dict) and "running_trade" in response2:
                        running_trades = response2.get("running_trade") or []
                    elif isinstance(response2, dict) and "data" in response2:
                        data2 = response2.get("data")
                        if isinstance(data2, dict) and "running_trade" in data2:
                            running_trades = data2.get("running_trade") or []
                        elif isinstance(data2, list):
                            running_trades = data2
                    elif isinstance(response2, list):
                        running_trades = response2

                    if debug:
                        print(f"[RUN] Retry returned {len(running_trades)} trades.")

            # finally if still empty -> stop
            if not running_trades:
                if debug:
                    print("[RUN] No more trades returned. Stopping.")
                break

            # extend and update cursor
            all_trades.extend(running_trades)

            # robustly parse last trade_number (string with commas maybe)
            last_trade = running_trades[-1]
            raw_tn = last_trade.get("trade_number") or last_trade.get("id") or last_trade.get("trade_no")
            try:
                # keep raw as string too, but store numeric for math
                tn_int = int(str(raw_tn).replace(",", ""))
                trade_number = tn_int
            except Exception:
                # if cannot parse, keep raw string (API might accept string)
                trade_number = raw_tn

            # break safety: if cursor didn't change, stop to avoid infinite loop
            if trade_number == previous_trade_number:
                if debug:
                    print("[RUN] Cursor did not advance (same as previous). Stopping to avoid infinite loop.")
                break

            previous_trade_number = trade_number

            if debug:
                print(f"[RUN] Scroll {scroll+1}/{max_scroll} → collected total {len(all_trades)} trades; next cursor={trade_number}")

            time.sleep(delay)

        return all_trades

    def get_filtered_running_trade_batches(self,
                                            max_scroll: int = 10,
                                            delay: float = 0.5,
                                            price_range_from: int | None = None,
                                            price_range_to: int | None = None,
                                            minimum_lot: int | None = None,
                                            action_type: str = "RUNNING_TRADE_ACTION_TYPE_ALL",
                                            debug: bool = False):
        """
        Fetch running-trade with server-side filters and cursor-pagination.
        Returns list of trade dicts.

        - max_scroll: number of pages to fetch (1 page = 50 items)
        - price_range_from / price_range_to: ints (sent to API)
        - minimum_lot: int (sent to API)
        - action_type: e.g. RUNNING_TRADE_ACTION_TYPE_ALL / BUY / SELL
        - delay: seconds between requests
        """
        all_trades = []
        trade_number = None
        previous_trade_number = None

        # prepare base query parameters
        base_q = f"sort=DESC&limit=50&order_by=RUNNING_TRADE_ORDER_BY_TIME&action_type={action_type}"
        if price_range_from is not None:
            base_q += f"&price_range_from={price_range_from}"
        if price_range_to is not None:
            base_q += f"&price_range_to={price_range_to}"
        if minimum_lot is not None:
            base_q += f"&minimum_lot={minimum_lot}"

        for scroll in range(max_scroll):
            q = base_q
            if trade_number is not None:
                q += f"&trade_number={trade_number}"

            endpoint = f"/order-trade/running-trade?{q}"
            url = f"{self.base_url}{endpoint}"

            if debug:
                print(f"[RT] Requesting: {url}")

            resp = self.stockbit_api_client.get(url)

            # defensive parse
            if isinstance(resp, str):
                try:
                    resp = json.loads(resp)
                except Exception:
                    resp = {}

            # extract trades robustly
            running_trades = []
            if isinstance(resp, dict):
                # common keys
                # The UI/previous examples: top-level key 'running_trade'
                if "running_trade" in resp:
                    running_trades = resp.get("running_trade") or []
                elif "data" in resp:
                    d = resp.get("data")
                    if isinstance(d, dict) and "running_trade" in d:
                        running_trades = d.get("running_trade") or []
                    elif isinstance(d, list):
                        running_trades = d
                else:
                    # attempt to find first list in response
                    for v in resp.values():
                        if isinstance(v, list):
                            running_trades = v
                            break
            elif isinstance(resp, list):
                running_trades = resp

            if debug:
                print(f"[RT] Batch {scroll+1} fetched items: {len(running_trades)}")

            # retry fallback using trade_number - 1 (exclusive cursor semantics) if empty
            if not running_trades and trade_number is not None:
                try:
                    tn_minus = int(str(trade_number).replace(",", "")) - 1
                except Exception:
                    tn_minus = None

                if tn_minus and tn_minus != previous_trade_number:
                    if debug:
                        print(f"[RT] Empty result for trade_number={trade_number}, retry with trade_number={tn_minus}")
                    endpoint2 = f"/order-trade/running-trade?{base_q}&trade_number={tn_minus}"
                    url2 = f"{self.base_url}{endpoint2}"
                    resp2 = self.stockbit_api_client.get(url2)
                    if isinstance(resp2, str):
                        try:
                            resp2 = json.loads(resp2)
                        except Exception:
                            resp2 = {}
                    if isinstance(resp2, dict) and "running_trade" in resp2:
                        running_trades = resp2.get("running_trade") or []
                    elif isinstance(resp2, dict) and "data" in resp2:
                        d2 = resp2.get("data")
                        if isinstance(d2, dict) and "running_trade" in d2:
                            running_trades = d2.get("running_trade") or []
                        elif isinstance(d2, list):
                            running_trades = d2
                    elif isinstance(resp2, list):
                        running_trades = resp2
                    if debug:
                        print(f"[RT] Retry returned {len(running_trades)} items.")

            if not running_trades:
                if debug:
                    print("[RT] No more trades returned; breaking.")
                break

            all_trades.extend(running_trades)

            # compute next cursor
            last_trade = running_trades[-1]
            raw_tn = last_trade.get("trade_number") or last_trade.get("id") or last_trade.get("trade_no")
            try:
                tn_int = int(str(raw_tn).replace(",", ""))
                next_cursor = tn_int
            except Exception:
                next_cursor = raw_tn

            if next_cursor == previous_trade_number:
                if debug:
                    print("[RT] Cursor did not advance. Stopping to avoid infinite loop.")
                break

            previous_trade_number = next_cursor
            trade_number = next_cursor

            if debug:
                print(f"[RT] Scroll {scroll+1}/{max_scroll} → collected total {len(all_trades)}; next_cursor={trade_number}")

            time.sleep(delay)

        return all_trades


    def get_stream_batches(self,
                        category="STREAM_CATEGORY_ALL_WATCHLIST",
                        last_stream_id=0,
                        last_reply=None,
                        limit=20,
                        max_pages=None,
                        delay=0.5,
                        debug=False):
        """
        Cursor-based fetcher for /stream/v3.
        Yields lists of normalized stream items.
        Safe: all helpers are local to avoid polluting module namespace.
        """

        def _parse_datetime(s):
            if not s:
                return None
            # try ISO-like
            try:
                # support "2026-02-13T15:20:00Z" and naive iso
                if s.endswith("Z"):
                    s2 = s.replace("Z", "+00:00")
                else:
                    s2 = s
                return datetime.fromisoformat(s2)
            except Exception:
                try:
                    # try integer unix ts
                    return datetime.fromtimestamp(int(s), tz=timezone.utc)
                except Exception:
                    return None

        def _extract_text(item):
            for k in ("message", "content", "text", "body", "caption"):
                v = item.get(k)
                if isinstance(v, str) and v.strip():
                    return v.strip()
            if "payload" in item and isinstance(item["payload"], dict):
                for k in ("text", "message"):
                    v = item["payload"].get(k)
                    if isinstance(v, str) and v.strip():
                        return v.strip()
            return ""

        def _extract_username(item):
            user = item.get("user") or item.get("author") or item.get("created_by")
            if isinstance(user, dict):
                return user.get("username") or user.get("name") or user.get("display_name")
            if isinstance(user, str):
                return user
            return item.get("username") or item.get("display_name")

        def _normalize_stream_item(raw):
            sid = raw.get("id") or raw.get("stream_id") or raw.get("post_id")
            created_at = raw.get("created_at") or raw.get("time") or raw.get("timestamp") or raw.get("created")
            dt = _parse_datetime(created_at)
            text = _extract_text(raw)
            username = _extract_username(raw)
            symbols = re.findall(r"\$[A-Z0-9\.]{1,10}", text or "")
            likes = raw.get("likes") or raw.get("like_count") or raw.get("likes_count") or 0
            comments = raw.get("comments") or raw.get("comment_count") or raw.get("replies_count") or 0

            return {
                "stream_id": str(sid) if sid is not None else None,
                "created_at": dt.isoformat() if dt else None,
                "username": username,
                "text": text,
                "symbols": symbols,
                "likes": int(likes) if isinstance(likes, (int, str)) and str(likes).isdigit() else likes,
                "comments": int(comments) if isinstance(comments, (int, str)) and str(comments).isdigit() else comments,
                "raw": raw
            }

        params = {
            "category": category,
            "last_stream_id": int(last_stream_id or 0),
            "limit": int(limit or 20)
        }
        if last_reply is not None:
            params["last_reply"] = int(last_reply)

        pages = 0
        while True:
            if debug and hasattr(self, "logger"):
                self.logger.info(f"[get_stream_batches] request params={params}")
            try:
                resp = self.stockbit_api_client.get("stream/v3", params=params)
                data = resp.json() if hasattr(resp, "json") else resp
            except Exception as e:
                if debug and hasattr(self, "logger"):
                    self.logger.exception("Error fetching stream, retrying once", exc_info=e)
                time.sleep(1.0)
                try:
                    resp = self.stockbit_api_client.get("stream/v3", params=params)
                    data = resp.json() if hasattr(resp, "json") else resp
                except Exception as e2:
                    if debug and hasattr(self, "logger"):
                        self.logger.exception("Second fetch failed; aborting", exc_info=e2)
                    break

            # permissive extraction of items list
            candidates = None
            if isinstance(data, dict):
                # case 1: { "streams": [...] }
                if "streams" in data and isinstance(data["streams"], list):
                    candidates = data["streams"]
                # case 2: { "data": { "streams": [...] } }
                elif "data" in data and isinstance(data["data"], dict):
                    inner = data["data"]
                    if "streams" in inner and isinstance(inner["streams"], list):
                        candidates = inner["streams"]
                    elif "items" in inner and isinstance(inner["items"], list):
                        candidates = inner["items"]
                # case 3: fallback scan
                if candidates is None:
                    for key in ("items", "results", "posts"):
                        if key in data and isinstance(data[key], list):
                            candidates = data[key]
                            break
            elif isinstance(data, list):
                candidates = data

            if not candidates:
                if debug and hasattr(self, "logger"):
                    self.logger.info("[get_stream_batches] no items found; stopping")
                break

            batch = []
            for raw in candidates:
                try:
                    norm = _normalize_stream_item(raw)
                    if not norm["stream_id"]:
                        gen = f"noid-{int(time.time()*1000)}"
                        norm["stream_id"] = gen
                    batch.append(norm)
                except Exception:
                    if debug and hasattr(self, "logger"):
                        self.logger.exception("failed to normalize an item; skipping")
                    continue

            if not batch:
                if debug and hasattr(self, "logger"):
                    self.logger.info("[get_stream_batches] normalized batch empty; stopping")
                break

            yield batch

            pages += 1
            if max_pages and pages >= max_pages:
                if debug and hasattr(self, "logger"):
                    self.logger.info(f"[get_stream_batches] reached max_pages={max_pages}; stopping")
                break

            last_item = candidates[-1]
            new_stream_id = last_item.get("id") or last_item.get("stream_id") or last_item.get("post_id")
            new_last_reply = last_item.get("last_reply") or last_item.get("reply_id") or last_item.get("last_reply_id")

            if new_stream_id is None:
                if debug and hasattr(self, "logger"):
                    self.logger.info("[get_stream_batches] last item has no id; stopping")
                break

            params["last_stream_id"] = int(new_stream_id)
            if new_last_reply is not None:
                params["last_reply"] = int(new_last_reply)

            time.sleep(delay)

    def get_broker_summary(
        self,
        ticker: str,
        date_from: str,
        date_to: str,
        transaction_type: str = "TRANSACTION_TYPE_GROSS",
        market_board: str = "MARKET_BOARD_ALL",
        investor_type: str = "INVESTOR_TYPE_ALL",
        limit: int = 25,
        debug: bool = False,
    ) -> Dict:
        """
        Fetch broker summary (market detector) for a single stock on a given date range.

        Endpoint  : GET /marketdetectors/{ticker}
        Defaults  : GROSS transaction, ALL market boards — matches Stockbit web UI default

        Returns dict with keys:
            'brokers_buy'     : list of buy-side broker records (sorted by B.val desc)
            'brokers_sell'    : list of sell-side broker records (sorted by S.val desc)
            'symbol'          : ticker
            'from'            : date_from
            'to'              : date_to
            'bandar_detector' : aggregated metrics dict (preserved as-is)

        Buy record fields  : netbs_broker_code, type, blot, blotv, bval, bvalv,
                             netbs_buy_avg_price, freq, netbs_date, netbs_stock_code
        Sell record fields : netbs_broker_code, type, slot, slotv, sval, svalv,
                             netbs_sell_avg_price, freq, netbs_date, netbs_stock_code

        Args:
            ticker           : stock ticker, e.g. "BBRI"
            date_from        : start date "YYYY-MM-DD"
            date_to          : end date "YYYY-MM-DD"
            transaction_type : "TRANSACTION_TYPE_GROSS" (default) or "TRANSACTION_TYPE_NET"
            market_board     : "MARKET_BOARD_ALL" (default) or "MARKET_BOARD_REGULER"
            investor_type    : "INVESTOR_TYPE_ALL" | "INVESTOR_TYPE_FOREIGN" | "INVESTOR_TYPE_LOCAL"
            limit            : brokers per side (default 25)
            debug            : print verbose info if True

        Returns:
            dict with broker summary data, or empty dict on failure.
        """
        params = (
            f"from={date_from}&to={date_to}"
            f"&transaction_type={transaction_type}"
            f"&market_board={market_board}"
            f"&investor_type={investor_type}"
            f"&limit={limit}"
        )
        url = f"{self.base_url}/marketdetectors/{ticker}?{params}"

        if debug:
            print(f"[BROKSUM] Requesting: {url}")

        resp = self.stockbit_api_client.get(url)

        if not resp or not isinstance(resp, dict):
            if debug:
                print(f"[BROKSUM] Empty or invalid response for {ticker}")
            return {}

        data = resp.get("data", {})
        if not data:
            if debug:
                print(f"[BROKSUM] No 'data' key in response for {ticker}")
            return {}

        broker_summary = data.get("broker_summary", {})
        bandar_detector = data.get("bandar_detector", {})

        result = {
            "symbol": broker_summary.get("symbol", ticker),
            "from": data.get("from", date_from),
            "to": data.get("to", date_to),
            "brokers_buy": broker_summary.get("brokers_buy") or [],
            "brokers_sell": broker_summary.get("brokers_sell") or [],
            "bandar_detector": bandar_detector,
        }

        if debug:
            print(
                f"[BROKSUM] {ticker}: "
                f"{len(result['brokers_buy'])} buyers, "
                f"{len(result['brokers_sell'])} sellers"
            )

        return result

    def get_broker_summary_all_stocks(
        self,
        tickers: List[str],
        date_from: str,
        date_to: str,
        transaction_type: str = "TRANSACTION_TYPE_GROSS",
        market_board: str = "MARKET_BOARD_ALL",
        investor_type: str = "INVESTOR_TYPE_ALL",
        limit: int = 25,
        delay: float = 0.5,
        debug: bool = False,
        on_progress=None,
    ) -> List[Dict]:
        """
        Fetch broker summary for a list of tickers and return rows ready for CSV export.

        Row structure mirrors the Stockbit web UI table exactly:
            BY, B.val, B.lot, B.freq, B.avg  |  SL, S.val, S.lot, S.freq, S.avg

        Each row = brokers_buy[i] ZIPped with brokers_sell[i] (paired by rank).
        If one side has fewer entries, the missing side's fields are left blank.

        Args:
            tickers       : list of ticker strings
            date_from     : start date "YYYY-MM-DD"
            date_to       : end date "YYYY-MM-DD"
            delay         : seconds between ticker requests (default 0.5)
            debug         : verbose logging
            on_progress   : optional callback(ticker, idx, total)

        Returns:
            list of flat dicts — one per rank row per ticker.
        """
        all_rows = []
        total = len(tickers)

        for idx, ticker in enumerate(tickers, start=1):
            if on_progress:
                on_progress(ticker, idx, total)
            else:
                logger.info(f"[BROKSUM] {idx}/{total} fetching {ticker}")

            summary = self.get_broker_summary(
                ticker=ticker,
                date_from=date_from,
                date_to=date_to,
                transaction_type=transaction_type,
                market_board=market_board,
                investor_type=investor_type,
                limit=limit,
                debug=debug,
            )

            if not summary:
                logger.warning(f"[BROKSUM] Skipped {ticker} - empty response")
                time.sleep(delay)
                continue

            buys  = summary.get("brokers_buy", [])
            sells = summary.get("brokers_sell", [])

            # ZIP by rank — pad the shorter list with empty dicts
            max_len = max(len(buys), len(sells))
            for i in range(max_len):
                b = buys[i]  if i < len(buys)  else {}
                s = sells[i] if i < len(sells) else {}

                # date comes from whichever side has data
                row_date = b.get("netbs_date") or s.get("netbs_date") or ""

                row = {
                    "stock_code" : summary["symbol"],
                    "date"       : row_date,
                    "from"       : summary["from"],
                    "to"         : summary["to"],
                    "rank"       : i + 1,
                    # --- BUY side (matches column: BY, B.val, B.lot, B.freq, B.avg) ---
                    "BY"         : b.get("netbs_broker_code", ""),
                    "BY_type"    : b.get("type", ""),
                    "B_val"      : b.get("bval", ""),
                    "B_lot"      : b.get("blot", ""),
                    "B_freq"     : b.get("freq", ""),
                    "B_avg"      : b.get("netbs_buy_avg_price", ""),
                    # --- SELL side (matches column: SL, S.val, S.lot, S.freq, S.avg) ---
                    "SL"         : s.get("netbs_broker_code", ""),
                    "SL_type"    : s.get("type", ""),
                    "S_val"      : s.get("sval", ""),
                    "S_lot"      : s.get("slot", ""),
                    "S_freq"     : s.get("freq", ""),
                    "S_avg"      : s.get("netbs_sell_avg_price", ""),
                }
                all_rows.append(row)

            time.sleep(delay)

        logger.info(f"[BROKSUM] Done. Total rows collected: {len(all_rows)}")
        return all_rows