from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderCreate, OrderResponse
from app.core.deps import get_current_user, require_role

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create_order(
    order_in: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    total_amount = 0
    order_items = []

    for item in order_in.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail="Not enough stock")

        unit_price = product.bulk_price if item.quantity >= product.min_order_quantity else product.price

        total_amount += unit_price * item.quantity

        product.stock -= item.quantity

        order_item = OrderItem(
            product_id=product.id,
            quantity=item.quantity,
            unit_price=unit_price,
        )
        order_items.append(order_item)

    new_order = Order(
        user_id=current_user.id,
        total_amount=total_amount,
        status="pending",
        items=order_items,
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.get("/", response_model=list[OrderResponse])
def list_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "admin":
        return db.query(Order).all()

    return db.query(Order).filter(Order.user_id == current_user.id).all()
