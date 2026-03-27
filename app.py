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
PORT = int(os.getenv("PORT", 5000))
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
def hello_world():
    return "Welcome to the AI Financial Analyst Assistant application."

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
