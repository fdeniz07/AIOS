from fastapi import FastAPI

app = FastAPI(title="AIOS Demo API")


@app.get("/")
def root():
    return {
        "application": "AIOS Demo API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }