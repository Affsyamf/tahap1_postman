from pydantic import BaseModel
from typing import Optional

class TugasCreate(BaseModel):
    judul: str
    nama: str
    deskripsi: Optional[str] = None
    
class Tugas(TugasCreate):
    id: int
    status: str = "belum selesai"
    
class Message(BaseModel):
    message: str