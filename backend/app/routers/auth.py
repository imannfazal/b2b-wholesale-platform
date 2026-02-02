from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["Auth"])

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

# Example route
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    # placeholder logic
    return {"id": 1, "email": user.email, "is_active": True}

@router.post("/login")
def login(user: UserLogin):
    return {"message": f"Logged in {user.email}"}
