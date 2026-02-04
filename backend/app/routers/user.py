from fastapi import APIRouter, Depends, HTTPException, status
from app.core.deps import get_current_user, require_role
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def read_current_user(user: User = Depends(get_current_user)):
    return {"email": user.email, "role": user.role, "is_active": user.is_active}

@router.get("/admin-only")
def admin_only(user: User = Depends(require_role("admin"))):
    return {"message": f"Welcome, admin {user.email}!"}
