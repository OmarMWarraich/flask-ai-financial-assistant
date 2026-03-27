import os
import traceback
import markdown

from io import BytesIO
from datetime import datetime, UTC
from flask import Flask, render_template, request, jsonify, send_file, session
from dotenv import load_dotenv
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from models import Holding, AnalysisHistory
from utils import get_stock_data, history_to_dataframe
from ai_module import dsp_financial_insight

# ---------------------------------------------------------------------
# Tasks 2, 3, and 4: Add Local Imports
# ---------------------------------------------------------------------
from extensions import db


# ---------------------------------------------------------------------
# Environment Configuration
# ---------------------------------------------------------------------
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_THIS_TO_A_RANDOM_VALUE")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///finance.db")
PORT = int(os.getenv("PORT", 5001))
DEBUG_MODE = os.getenv("FLASK_ENV") == "development"

# ---------------------------------------------------------------------
# Flask Application Setup
# ---------------------------------------------------------------------
app = Flask(__name__)
app.config.update(
    SECRET_KEY=SECRET_KEY,
    SQLALCHEMY_DATABASE_URI=DATABASE_URL,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(app)

# Ensure tables exist
with app.app_context():
    db.create_all()

# ---------------------------------------------------------------------
# Task 5: Flask Frontend Route Implementation for the AI Financial Analyst Assistant
# ---------------------------------------------------------------------

@app.route("/")
def index():
    """
    Home page displaying live data for default tickers.
    """
    default_tickers = [
        "AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NFLX",
        "JPM", "V", "PG", "NVDA", "ADBE", "CRM", "INTC",
        "CSCO", "PEP", "COST", "KO", "PFE", "MRK", "UNH",
        "HD", "WMT", "DIS", "NKE", "BA", "MCD", "SBUX",
        "IBM", "ORCL", "CMCSA", "T", "VZ", "BABA", "XOM",
        "CVX", "WFC", "GS", "MS", "AXP", "BAC", "PYPL",
        "QCOM", "TXN", "AMAT", "GILD", "BIIB", "LMT", "GE"
    ]

    stocks = []
    for ticker in default_tickers:
        try:
            stocks.append(get_stock_data(ticker))
        except Exception as e:
            print(f"[index] Error fetching {ticker}: {e}")
            stocks.append({
                "ticker": ticker, "company": "N/A", "price": None,
                "change_pct": None, "pe_ratio": None, "beta": None,
                "sector": "N/A"
            })

    return render_template("index.html", default_stocks=stocks)


@app.route("/portfolio")
def portfolio_page():
    """
    Display user's portfolio with live prices and total valuation.
    """
    holdings = Holding.query.order_by(Holding.ticker).all()
    total_value = 0.0
    enriched = []

    for h in holdings:
        try:
            data = get_stock_data(h.ticker)
        except Exception as e:
            print(f"[portfolio_page] Error fetching {h.ticker}: {e}")
            data = {"price": 0.0}

        price = data.get("price") or 0.0
        value = round(price * h.quantity, 2)
        total_value += value

        enriched.append({
            "id": h.id,
            "ticker": h.ticker,
            "quantity": h.quantity,
            "price": price,
            "value": value,
        })

    return render_template("portfolio.html", holdings=enriched, total_value=round(total_value, 2))

@app.route("/history")
def history_page():
    """
    Display recent AI-generated financial analyses.
    """
    items = AnalysisHistory.query.order_by(AnalysisHistory.created_at.desc()).limit(50).all()
    return render_template("analysis.html", items=items)

# ---------------------------------------------------------------------
# Task 6: Implement DSPy Stock Analysis and Insight Summary Routes
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Task 7: Implement Portfolio Management Routes
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Task 8: Implement Portfolio PDF Report Generation Route
# ---------------------------------------------------------------------


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
