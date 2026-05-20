from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
import jinja2
from starlette.middleware.sessions import SessionMiddleware

import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key="some-random-string")


# Setup Jinja2 environment directly
loader = jinja2.FileSystemLoader("templates")
env = jinja2.Environment(loader=loader)

# Helper to render templates
def render_template(template_name: str, context: dict):
    template = env.get_template(template_name)
    return HTMLResponse(content=template.render(context))

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Get the last result from the session if it exists (flash message)
    last_result = request.session.get("last_result")
    if last_result:
        # Clear the message from the session
        del request.session["last_result"]
        
    recent_links = request.session.get("recent_links", [])
    
    # Combine contexts for rendering
    context = {"request": request, "recent_links": recent_links}
    if last_result:
        context.update(last_result)
        
    return render_template("index.html", context)

@app.post("/shorten", response_class=RedirectResponse)
async def create_url(request: Request, long_url: str = Form(...), db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db=db, url=schemas.URLCreate(long_url=long_url))
    
    base_url = str(request.base_url)
    short_url = base_url + db_url.short_code
    
    new_link = {"long_url": long_url, "short_url": short_url}

    # Get recent links from session
    recent_links = request.session.get("recent_links", [])

    # Remove the link if it already exists to avoid duplicates and move it to the top
    recent_links = [link for link in recent_links if link["short_url"] != short_url]

    # Add the new link to the beginning of the list
    recent_links.insert(0, new_link)

    # Update the session, keeping only the 5 most recent links
    request.session["recent_links"] = recent_links[:5]
    
    # Store the result for the next page load (flash message)
    request.session["last_result"] = {
        "short_url": short_url,
        "long_url": long_url
    }
    
    # Redirect to the main page
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/{short_code}")
async def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_short_code(db, short_code=short_code)
    if db_url:
        return RedirectResponse(url=db_url.long_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
    
    # You could render a "not found" page here
    return HTMLResponse(content="<h1>URL not found</h1>", status_code=404)
