# FastAPI URL Shortener

A simple, fast, and modern URL shortener web application built with Python and the FastAPI framework.

This project provides a clean interface to turn long, cumbersome URLs into short, manageable links. It also keeps a history of your most recently created links for easy access.

## Features

- **Fast URL Shortening:** Quickly generates a random 6-character code for any long URL.
- **Reliable Redirection:** Short links use a permanent (301) redirect to the original URL.
- **Recent Link History:** The 5 most recently created short URLs are displayed on the main page for the duration of your session. Duplicate URLs are automatically deduplicated.
- **Clear History Button:** Easily clear all your recent link history with a single click.
- **Favorites Management:** Mark URLs as favorites using the star icon (⭐). Favorite links are persisted in the database and displayed in the Favorites section.
- **Modern Backend:** Built with the high-performance FastAPI framework.
- **Robust Database Interaction:** Uses SQLAlchemy and Pydantic for type-safe database operations with SQLite.
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
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

Once the setup is complete, you can run the application using Uvicorn. The `--reload` flag will automatically restart the server when you make code changes.

```bash
uvicorn main:app --reload
```

The application will be available at **http://127.0.0.1:8000**.

## Usage

### Main Features

1. **Shorten a URL:**
   - Enter any long URL in the input field and click "Shorten"
   - A shortened URL is generated and displayed
   - The link is added to your recent links history

2. **Manage Recent Links:**
   - Your 5 most recently created links are displayed in the "Recently Created Links" section
   - Click the ⭐ star icon next to a link to add it to your favorites
   - Click "Clear History" to remove all recent links at once

3. **Manage Favorites:**
   - Favorite URLs are saved in the database and persist across sessions
   - The "Favorites" section displays all your bookmarked links
   - Click the ⭐ star icon on a favorite to remove it from favorites

## Database

The application uses **SQLite** for persistent storage of favorites and URL mappings.

**Database file location:**
```
url_shortener.db
```

**Database Schema:**

The `urls` table contains:
- `id` (Integer, primary key)
- `long_url` (String) - Original URL
- `short_code` (String, unique) - Generated short code
- `is_active` (Boolean) - Whether the link is active
- `is_favorite` (Boolean) - Whether the link is marked as favorite

**Viewing the Database:**

You can view and manage the database using [DB Browser for SQLite](https://sqlitebrowser.org/):
1. Download and install DB Browser for SQLite
2. Open the application and select "File" → "Open Database"
3. Navigate to the `url_shortener.db` file in your project directory
4. Browse tables, rows, and data in a user-friendly interface

