from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "service-a", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/a")
def service_a():
    return {"service": "service-a", "path": "/a", "status": "running"}
