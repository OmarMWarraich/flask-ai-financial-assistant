# AI Financial Assistant

A Flask-based financial assistant project that combines stock-data utilities, AI analysis scaffolding, and a SQLite-backed local development setup.

## Current State

This repository is partially scaffolded.

- The Flask app entrypoint is `app.py`.
- Environment variables are loaded from `.env`.
- SQLAlchemy is initialized and `db.create_all()` runs on startup.
- The root route `/` is implemented and currently returns a plain welcome message.
- Additional templates and modules for stock analysis, insight summaries, portfolio management, and PDF generation are present, but the corresponding routes and model logic are not fully implemented yet.

## Tech Stack

- Flask
- Flask-SQLAlchemy
- python-dotenv
- SQLite
- pandas
- yfinance
- OpenAI Python SDK
- DSPy
- Markdown
- ReportLab

## Project Structure

```text
.
├── app.py
├── ai_module.py
├── extensions.py
├── models.py
├── utils.py
├── static/
└── templates/
```

## Local Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

Install the pinned dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Example:

```dotenv
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=sqlite:///finance.db
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=replace_with_a_random_secret
PORT=5000
```

Notes:

- `DATABASE_URL=sqlite:///finance.db` creates or uses a local SQLite database file named `finance.db`.
- Keep `.env` out of version control.
- Use a real random value for `SECRET_KEY`.

## Running the App

From the project root:

```bash
source .venv/bin/activate
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

You can also run it with Flask CLI:

```bash
source .venv/bin/activate
flask run
```

## Database Behavior

- The app uses SQLAlchemy with SQLite.
- On startup, the app calls `db.create_all()`.
- SQLite will create the database file automatically when the app connects and writes to it.
- Tables are only created for models that actually exist and are imported before `create_all()` runs.

At the moment, `models.py` is only a placeholder, so you should not expect meaningful tables yet.

## Implemented Files

- `app.py`: Flask app setup, env loading, SQLAlchemy configuration, and development server startup.
- `extensions.py`: shared SQLAlchemy instance.
- `ai_module.py`: AI analysis scaffolding using DSPy and the OpenAI SDK.
- `utils.py`: placeholder for stock data utilities.
- `templates/`: scaffolded HTML templates for analysis and portfolio views.

## Known Limitations

- Most application routes described by the templates are not wired up yet.
- `models.py` does not define database models yet.
- This is suitable for local development only in its current form.

## Development Notes

- If you previously tried `flasker`, it is not required to run this repository.
- Running `python app.py` is the most direct way to start the current app.
- For production use, add proper configuration management, migrations, tests, and a production WSGI server.