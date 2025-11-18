from fastapi import APIRouter, HTTPException, status
from typing import List
import app.services as services
from app.models import Tugas, TugasCreate, Message


router = APIRouter(
    prefix="/tugas",
    tags=["Tugas"]
)

# dekorator
@router.post("/", response_model = Tugas, status_code=status.HTTP_201_CREATED)
def create_tugas_route(tugas_data: TugasCreate):
    return services.create_tugas_service(tugas_data)

@router.get("/", response_model=List[Tugas])
def read_all_tugas_route():
    return services.get_all_tugas_service()

@router.get("/{tugas_id}", response_model=Tugas)
def read_one_tugas_route(tugas_id: int):
    tugas = services.get_tugas_by_id_service(tugas_id)
    if not tugas:
        raise HTTPException(status_code=404, detail="Tugas tidak ditemukan")
    return tugas

@router.put("/{tugas_id}", response_model=Tugas)
def update_tugas_route(tugas_id: int, data_update: TugasCreate):
    tugas_updated = services.update_tugas_service(tugas_id, data_update)
    if not tugas_updated:
        raise HTTPException(status_code=404, detail="Tugas tidak ditemukan")
    return tugas_updated
    
@router.delete("/{tugas_id}", response_model=Message)
def delete_tugas_route(tugas_id: int):
    success = services.delete_tugas_service(tugas_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tugas tidak ditemukan")
    return {"message": f"tugas dengan id {tugas_id} berhasil dihapus"}