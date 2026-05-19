from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
import jinja2

import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
    return render_template("index.html", {"request": request})

@app.post("/shorten", response_class=HTMLResponse)
async def create_url(request: Request, long_url: str = Form(...), db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db=db, url=schemas.URLCreate(long_url=long_url))
    
    base_url = str(request.base_url)
    short_url = base_url + db_url.short_code
    
    return render_template("index.html", {
        "request": request,
        "short_url": short_url,
        "long_url": long_url
    })

@app.get("/{short_code}")
async def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_short_code(db, short_code=short_code)
    if db_url:
        return RedirectResponse(url=db_url.long_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
    
    # You could render a "not found" page here
    return HTMLResponse(content="<h1>URL not found</h1>", status_code=404)
