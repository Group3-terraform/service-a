from fastapi import FastAPI

app = FastAPI()

@app.get("/a")
def get_root():
    return {"service": "service-a", "status": "running"}

@app.get("/a/health")
def get_health():
    return {"status": "ok"}

@app.get("/a/info")
def get_info():
    return {"service": "service-a", "path": "/a/info", "status": "running"}

@app.get("/a/info/g3")
def get_info_g3():
    return {"service": "service-a", "path": "/a/info/g3", "status": "running", "group": "devops-team-3"}

@app.get("/a/info/g4")
def get_info_g4():
    return {"service": "service-a", "path": "/a/info/g4", "status": "running", "group": "devops-team-4"}
