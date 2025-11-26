# CI/CD test


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend running on EC2"}

@app.get("/health")
def health():
    return {"status": "healthy"}
