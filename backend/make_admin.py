# make_admin.py
from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Config
ADMIN_EMAIL = "iman@gmail.com"
DEFAULT_PASSWORD = "secret123"

# Open DB session
db = SessionLocal()

# Check if user exists
user = db.query(User).filter(User.email == ADMIN_EMAIL).first()

if not user:
    # Create user if not exists
    hashed_password = pwd_context.hash(DEFAULT_PASSWORD[:72])
    user = User(
        email=ADMIN_EMAIL,
        hashed_password=hashed_password,
        is_active=True,
        role="admin"  # directly assign string role
    )
    db.add(user)
    db.commit()
    print(f"✅ User {ADMIN_EMAIL} created with default password and admin role")
else:
    # Promote to admin if exists
    if user.role != "admin":
        user.role = "admin"
        db.commit()
        print(f"✅ User {ADMIN_EMAIL} promoted to admin")
    else:
        print(f"ℹ️ User {ADMIN_EMAIL} already has admin role")

db.close()
