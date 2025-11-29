from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "service-a", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "service-a"}
