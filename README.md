# MyWeb Portfolio (Flask)

Personal portfolio website built with Flask and Jinja templates.

## Features

- Responsive portfolio landing page
- Dynamic profile data from `app.py`
- Sections for skills, experience, projects, education, and contact
- Styled with custom CSS in `static/css/style.css`

## Project Structure

- `app.py` - Flask app and portfolio data
- `templates/index.html` - Main HTML template
- `static/css/style.css` - Styling
- `Procfile` - Production process command (`gunicorn app:app`)

## Requirements

- Python 3.9+ (recommended)
- pip

## Run Locally

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install flask gunicorn
```

3. Start the app:

```bash
python app.py
```

4. Open:

`http://127.0.0.1:1116`

## Environment Variables

- `PORT` - App port (default: `1116`)
- `FLASK_DEBUG` - Enable debug mode (`1`, `true`, or `yes`)

## Deploy

This app is configured for WSGI deployment via:

`web: gunicorn app:app`

Use this in platforms like Heroku or similar services.
