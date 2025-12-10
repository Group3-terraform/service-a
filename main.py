from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "service-a", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# so external /a returns 200 as well
@app.get("/a")
def service_a():
    return {"service": "service-a", "path": "/a", "status": "running"}
