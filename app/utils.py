import app.database as db

def get_next_id():
    if not db.list_tugas:
        return 1
    
    last_id = db.list_tugas[-1].id
    return last_id + 1