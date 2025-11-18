from fastapi import FastAPI
from app.routes import tugas

app = FastAPI(
    title="aplikasi Manajemen Tugas",
    description="api untuk mengelola tugas",
)

app.include_router(tugas.router)

@app.get("/")
def read_root():
    return {"message": "aplikasi Manajemen Tugas!"}