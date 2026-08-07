from database import SessionLocal
from models.user import User

db = SessionLocal()

user = User(
    email="test@example.com",
    first_name="Yessir",
    height=169,
    weight=64,
    goal_weight=78
)

db.add(user)
db.commit()
db.close()

print("User inserted")
