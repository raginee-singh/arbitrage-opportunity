import logging
from services.binance_services import BinanceService
from services.solana_services import SolanaService

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ArbitrageService:
    def __init__(self):
        try:
            self.binance = BinanceService()
            self.solana_dex = SolanaService()
            logger.info("Initialized ArbitrageService with BinanceService and SolanaService.")
        except Exception as e:
            logger.error(f"Error initializing ArbitrageService: {e}")
            raise

    def find_arbitrage_opportunities(self, binance_pairs, solana_pairs):
        try:
            logger.info("Finding arbitrage opportunities.")
            common_pairs = set(binance_pairs.keys()).intersection(solana_pairs.keys())
            opportunities = []

            for pair in common_pairs:
                binance_price = binance_pairs[pair]
                solana_price = solana_pairs[pair]
                
                # Log the pair and prices
                logger.info(f"Pair: {pair}, Binance Price: {binance_price}, Solana Price: {solana_price}")

                # Binance to Solana arbitrage
                if binance_price < solana_price:
                    profit = (solana_price - binance_price) - (binance_price * 0.001) - (solana_price * 0.003)
                    if profit > 0:
                        opportunities.append({
                            "pair": pair,
                            "direction": "Binance -> Solana",
                            "profit": round(profit, 2)
                        })

                # Solana to Binance arbitrage
                elif solana_price < binance_price:
                    profit = (binance_price - solana_price) - (solana_price * 0.003) - (binance_price * 0.001)
                    if profit > 0:
                        opportunities.append({
                            "pair": pair,
                            "direction": "Solana -> Binance",
                            "profit": round(profit, 2)
                        })

            return opportunities
        except Exception as e:
            logger.error(f"Error finding arbitrage opportunities: {e}")
            raise
