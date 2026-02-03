from fastapi import APIRouter, Depends
from app.core.deps import get_current_user, require_role
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role.name,
    }


@router.get("/admin-only")
def admin_only(user: User = Depends(require_role("ADMIN"))):
    return {"message": "Welcome admin"}
