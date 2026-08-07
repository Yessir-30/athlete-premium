from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Integer)
    muscle_mass = Column(String)
    comment = Column(String)
