import app.database as db
from app.models import Tugas, TugasCreate
from app.utils import get_next_id
from typing import List

# membuat tugas baru
def create_tugas_service(data_tugas: TugasCreate) -> Tugas:
    tugas_baru = Tugas(
        id=get_next_id(),
        judul=data_tugas.judul,
        deskripsi=data_tugas.deskripsi,
        nama=data_tugas.nama
    )
    db.list_tugas.append(tugas_baru)
    return tugas_baru

# mengambil semua tugas
def get_all_tugas_service() -> List[Tugas]:
    return db.list_tugas


# mengambil tugas berdasarkan id
def get_tugas_by_id_service(tugas_id: int) -> Tugas | None:
    for tugas in db.list_tugas:
        if tugas.id == tugas_id:
            return tugas
    return None
    
# ubah tugas
def update_tugas_service(tugas_id: int, data_update: TugasCreate) -> Tugas | None:
    tugas = get_tugas_by_id_service(tugas_id)
    if not tugas:
        return None
    
    tugas.judul = data_update.judul
    tugas.nama = data_update.nama
    tugas.deskripsi = data_update.deskripsi
    return tugas


# hapus tugas
def delete_tugas_service(tugas_id: int) -> bool:
    tugas = get_tugas_by_id_service(tugas_id)
    if not tugas:
        return False
    
    db.list_tugas.remove(tugas)
    return True