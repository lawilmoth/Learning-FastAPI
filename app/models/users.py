from sqlalchemy import Column, Integer, String
from ..database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String, index=True)

    posts = relationship("Post", back_populates="author")