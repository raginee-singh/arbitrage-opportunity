import requests
import os
import logging
from dotenv import load_dotenv
from config.charges_config import BINANCE_FEE

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BinanceService:
    BASE_URL = "https://api.binance.com/api/v3"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

    def get_usdc_pairs(self):
        try:
            logger.info("Fetching USDC trading pairs from Binance")
            response = requests.get(f"{self.BASE_URL}/ticker/price")
            response.raise_for_status()

            prices = response.json()
            usdc_pairs = {
                item['symbol']: float(item['price'])
                for item in prices
                if 'USDC' in item['symbol']
            }
            logger.info("Successfully fetched USDC pairs from Binance")
            return usdc_pairs
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from Binance API: {e}")
            raise

    def calculate_binance_fee(self, price):
        try:
            logger.info("Calculating Binance fee")
            fee_applied_price = price * (1 - BINANCE_FEE)
            logger.info("Successfully calculated Binance fee")
            return fee_applied_price
        except Exception as e:
            logger.error(f"Error calculating Binance fee: {e}")
            raise
