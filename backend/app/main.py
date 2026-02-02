from fastapi import FastAPI

app = FastAPI(title="B2B Wholesale API")

@app.get("/")
def health_check():
    return {"status": "running"}
