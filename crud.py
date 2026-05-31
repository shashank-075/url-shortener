from sqlalchemy.orm import Session
import random
import string
import models, schemas

def get_url_by_long_url(db: Session, long_url: str):
    return db.query(models.URL).filter(models.URL.long_url == long_url).first()

def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

def create_short_url(db: Session, url: schemas.URLCreate):
    db_url = get_url_by_long_url(db, long_url=url.long_url)
    if db_url:
        return db_url
    
    short_code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    db_url = models.URL(long_url=url.long_url,short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_favorite_urls(db: Session):
    return db.query(models.URL).filter(models.URL.is_favorite == True).all()

def update_favorite_status(db: Session, short_code: str, is_favorite: bool):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url:
        db_url.is_favorite = is_favorite
        db.commit()
        db.refresh(db_url)
    return db_url