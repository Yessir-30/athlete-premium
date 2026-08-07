from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Nutrition(Base):
    __tablename__ = "nutrition"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    calories = Column(Integer)
    proteins = Column(Integer)
    hydration = Column(String)
