from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_type = Column(String)
    notes = Column(String)
