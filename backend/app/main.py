# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Import models (only needed for metadata creation)
from app.models import user as user_model, product as product_model

# Import routers
from app.routers import auth, user, product, order

app = FastAPI(title="B2B Wholesale API")

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(user.router)   # Users router
app.include_router(product.router) # Products router
app.include_router(order.router) # Orders router

# Health check endpoint
@app.get("/")
def health_check():
    return {"status": "running"}
