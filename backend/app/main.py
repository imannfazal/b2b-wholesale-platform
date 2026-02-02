from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, role
from app.routers import auth

app = FastAPI(title="B2B Wholesale API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
def health_check():
    return {"status": "running"}
