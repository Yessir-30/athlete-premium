from database import Base, engine
from models.user import User

Base.metadata.create_all(bind=engine)
