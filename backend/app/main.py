# app/main.py
from fastapi import FastAPI
from app.database import engine, Base

# Import models (only needed for metadata creation)
from app.models import user as user_model, role as role_model, product as product_model

# Import routers
from app.routers import auth, user, product

app = FastAPI(title="B2B Wholesale API")

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(user.router)   # Users router
app.include_router(product.router) # Products router

# Health check endpoint
@app.get("/")
def health_check():
    return {"status": "running"}
