import logging
from config.charges_config import SOLANA_FEE, SOLANA_TRANSACTION_COST

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SolanaService:
    def __init__(self):
        self.mocked_data = {
            "INJUSDC": 34.14,
            "SOLUSDC": 189.70,
            "USDCUSDT": 1.00,
            "MATICUSDC": 0.38,
            "AVAXUSDC": 37.37,
            "DOTUSDC": 6.73,
            "USDCXRP": 2.52,
            "USDCETH": 3285.10,
            "USDCLTC": 102.91,
            "USDCUSDT": 1.00,
        }

    def get_usdc_pairs(self):
        try:
            logger.info("Fetching USDC trading pairs from Solana DEX")
            return self.mocked_data
        except Exception as e:
            logger.error(f"Error fetching USDC pairs: {e}")
            raise

    def calculate_solana_fee(self, price):
        try:
            fee = price * (1 - SOLANA_FEE)
            logger.info(f"Calculated Solana fee for price {price}: {fee}")
            return fee
        except Exception as e:
            logger.error(f"Error calculating Solana fee: {e}")
            raise

    def calculate_transaction_cost(self):
        try:
            logger.info("Calculating Solana transaction cost")
            return SOLANA_TRANSACTION_COST
        except Exception as e:
            logger.error(f"Error calculating transaction cost: {e}")
            raise
