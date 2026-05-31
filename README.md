# FastAPI URL Shortener

A simple, fast, and modern URL shortener web application built with Python and the FastAPI framework.

This project provides a clean interface to turn long, cumbersome URLs into short, manageable links. It also keeps a history of your most recently created links for easy access.

## Features

- **Fast URL Shortening:** Quickly generates a random 6-character code for any long URL.
- **Reliable Redirection:** Short links use a permanent (301) redirect to the original URL.
- **Recent Link History:** The 5 most recently created short URLs are displayed on the main page for the duration of your session.
- **Modern Backend:** Built with the high-performance FastAPI framework.
- **Robust Database Interaction:** Uses SQLAlchemy and Pydantic for type-safe database operations.
- **No-Refresh Resubmissions:** Implements the Post/Redirect/Get (PRG) pattern to prevent duplicate links from being created when the page is refreshed.

## Technology Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [SQLAlchemy](https://www.sqlalchemy.org/) with SQLite
- **Data Validation:** [Pydantic](https://pydantic-docs.helpmanual.io/)
- **Server:** [Uvicorn](https://www.uvicorn.org/)
- **Templating:** [Jinja2](https://jinja.palletsprojects.com/)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd url-shortener
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    The `requirements.txt` file contains the base packages. You will also need `starlette`, `itsdangerous`, and `python-multipart` for the session feature to work correctly.

    ```bash
    pip install -r requirements.txt
    pip install "starlette" "itsdangerous" "python-multipart"
    ```

## How to Run the Application

Once the setup is complete, you can run the application using Uvicorn. The `--reload` flag will automatically restart the server when you make code changes.

```bash
uvicorn main:app --reload
```

The application will be available at **http://127.0.0.1:8000**.

