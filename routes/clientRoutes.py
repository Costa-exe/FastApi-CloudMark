from fastapi import APIRouter
from services.service import Service
from models.clientModel import Client

router = APIRouter(prefix="/clients", tags=["Clients API"])

@router.get("")
async def get_clients(client_id : str | None = None):
    try:
        if client_id:
            return Service.get_client_by_id_service(client_id)
        return Service.get_all_clients_service()
    except Exception as e:
        return e

@router.delete("/delete")
async def delete_client(client_id: str):
    return Service.delete_client_by_id_service(client_id)

@router.post("/add")
async def add_client(client : Client):
    return Service.create_new_client(client)

@router.put("/update")
async def update_client(client_id : str, new_data : Client):
    return Service.update_client(client_id, new_data)