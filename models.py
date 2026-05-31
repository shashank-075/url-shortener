from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    short_code = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_favorite = Column(Boolean, default=False)
    