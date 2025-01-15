# Arbitrage Opportunity Finder

A Python-based web application that fetches USDC trading pairs from Binance and Solana-based DEX APIs and identifies arbitrage opportunities between the two platforms. The project includes a Flask backend and a simple UI to display the data in a table format with buttons to trigger the API calls.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [UI Description](#ui-description)
- [Logging and Error Handling](#logging-and-error-handling)
- [License](#license)

---

## Project Overview
This application helps identify arbitrage opportunities between Binance and Solana-based decentralized exchanges by comparing USDC trading pair prices. It provides three APIs that:
1. Fetch USDC trading pairs from Binance.
2. Fetch USDC trading pairs from Solana DEX.
3. Identify arbitrage opportunities between the two platforms.

The project includes a simple UI that displays the data in a table format and uses buttons to trigger API calls.

---

## Technologies Used
- Python (Flask)
- HTML/CSS/JavaScript for the UI
- Flask-Limiter for rate limiting
- Dotenv for environment variables
- Logging for error tracking

---

## Features
- Fetch real-time USDC trading pairs from Binance and Solana DEX.
- Identify arbitrage opportunities and calculate potential profits.
- Simple UI to interact with the APIs.
- Rate limiting to prevent excessive API requests.
- Detailed logging and exception handling.

---

## Folder Structure

arbitrage-project/
├── controllers/
│   └── arbitrage_controller.py
├── services/
│   ├── binance_services.py
│   ├── solana_services.py
│   └── arbitrage_services.py
├── config/
│   └── charges_config.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── app.js
├── .env
├── requirements.txt
├── README.md
└── venv/

---

## Setup Instructions

### Clone the repository:
git clone https://github.com/novapulseio/coding-assignment
cd arbitrage-project


### Install dependencies:
pip install -r requirements.txt

### Set up your .env file:
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
GLOBAL_RATE_LIMIT=100 per hour
BINANCE_RATE_LIMIT=30 per minute
SOLANA_RATE_LIMIT=2 per minute
ARBITRAGE_RATE_LIMIT=15 per minute

### Run the Flask app:
set PYTHONPATH=%cd%
python -m controllers.arbitrage_controller

### Open the app in your browser:
Go to `http://localhost:5000` to access the UI.


## Environment Variables
| Variable Name        | Description                         |
|----------------------|-------------------------------------|
| `BINANCE_API_KEY`    | Your Binance API key                |
| `BINANCE_SECRET_KEY` | Your Binance secret key             |
| `GLOBAL_RATE_LIMIT`  | Global rate limit for all APIs      |
| `BINANCE_RATE_LIMIT` | Rate limit for the Binance API      |
| `SOLANA_RATE_LIMIT`  | Rate limit for the Solana API       |
| `ARBITRAGE_RATE_LIMIT`| Rate limit for the arbitrage API    |


## API Endpoints

| Endpoint                         | Method | Description                      | Rate Limit     |
|----------------------------------|--------|----------------------------------|----------------|
| `/api/v1/markets/binance`        | GET    | Fetch USDC trading pairs from Binance | 30 per minute  |
| `/api/v1/markets/solana`         | GET    | Fetch USDC trading pairs from Solana DEX | 2 per minute   |
| `/api/v1/arbitrage-opportunities` | GET    | Find arbitrage opportunities      | 15 per minute  |



## UI Description
The UI is a simple HTML/CSS/JavaScript interface located in the `templates` and `static` folders.

### UI Features:
- Three buttons to trigger each API endpoint.
- Table format to display the fetched data.
- Basic styling using `style.css`.
- Dynamic interaction using `app.js`.



## Logging and Error Handling
The application includes detailed logging and exception handling to track errors and monitor API requests.

- Logs are set to `INFO` level.
- Key operations are wrapped in `try-except` blocks to handle exceptions gracefully.
- Error messages are logged and returned in the API responses.

Example log output:
```log
2025-01-13 10:30:00 - INFO - Starting Flask app
2025-01-13 10:30:10 - INFO - Fetching Binance USDC pairs
2025-01-13 10:30:11 - INFO - Successfully fetched Binance data
2025-01-13 10:30:12 - INFO - Finding arbitrage opportunities
2025-01-13 10:30:13 - INFO - Successfully found arbitrage opportunities
```

---

## License
This project is open-source and available under the MIT License.