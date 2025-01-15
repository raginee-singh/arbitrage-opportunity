import os
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.binance_services import BinanceService
from services.solana_services import SolanaService
from services.arbitrage_services import ArbitrageService

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Load configuration from .env
app.config['GLOBAL_RATE_LIMIT'] = os.getenv("GLOBAL_RATE_LIMIT", "100 per hour")
app.config['BINANCE_RATE_LIMIT'] = os.getenv("BINANCE_RATE_LIMIT", "30 per minute")
app.config['SOLANA_RATE_LIMIT'] = os.getenv("SOLANA_RATE_LIMIT", "2 per minute")
app.config['ARBITRAGE_RATE_LIMIT'] = os.getenv("ARBITRAGE_RATE_LIMIT", "15 per minute")
debug_mode = os.getenv("FLASK_DEBUG", "True").lower() == "true"

# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[app.config['GLOBAL_RATE_LIMIT']]  # Set a global rate limit
)
limiter.init_app(app)

# Initialize service instances
binance_service = BinanceService()
solana_service = SolanaService()
arbitrage_service = ArbitrageService()

# Route to serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define routes with rate limiting and logging
@app.route('/api/v1/markets/binance', methods=['GET'])
@limiter.limit(app.config['BINANCE_RATE_LIMIT'])  # Limit requests to 30 per minute
def get_binance_data():
    try:
        usdc_pairs = binance_service.get_usdc_pairs()
        logger.info("Successfully fetched Binance data")
        return jsonify({"status": "success", "data": usdc_pairs}), 200
    except Exception as e:
        logger.error(f"Error fetching Binance data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/v1/markets/solana', methods=['GET'])
@limiter.limit(app.config['SOLANA_RATE_LIMIT'])  # Custom limit for Solana API
def get_solana_data():
    try:
        usdc_pairs = solana_service.get_usdc_pairs()
        logger.info("Successfully fetched Solana data")
        return jsonify({"status": "success", "data": usdc_pairs}), 200
    except Exception as e:
        logger.error(f"Error fetching Solana data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/v1/arbitrage-opportunities', methods=['GET'])
@limiter.limit(app.config['ARBITRAGE_RATE_LIMIT'])  # Custom limit for arbitrage endpoint
def get_arbitrage_opportunities():
    try:
        binance_pairs = binance_service.get_usdc_pairs()
        solana_pairs = solana_service.get_usdc_pairs()
        opportunities = arbitrage_service.find_arbitrage_opportunities(binance_pairs, solana_pairs)
        logger.info("Successfully found arbitrage opportunities")
        return jsonify({"status": "success", "data": opportunities}), 200
    except Exception as e:
        logger.error(f"Error finding arbitrage opportunities: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    logger.info("Starting Flask app")
    app.run(debug=debug_mode)
