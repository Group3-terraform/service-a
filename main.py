from fastapi import FastAPI

app = FastAPI()

@app.get("/a")
def root():
    return {"service": "service-a", "status": "running"}

@app.get("/a/health")
def health():
    return {"status": "ok"}

@app.get("/a/info")
def info():
    return {"service": "service-a", "path": "/a/info", "status": "running"}

@app.get("/a/info/g3")
def info():
    return {"service": "service-a", "path": "/a/info", "status": "running", "group": "devops-team-3"}

@app.get("/a/info/g4")
def info():
    return {"service": "service-a", "path": "/a/info", "status": "running", "group": "devops-team-4"}
