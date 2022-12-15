from fastapi import APIRouter
from services.service import Service
from models.clientModel import Client

router = APIRouter(prefix="/clients", tags=["Clients API"])

@router.get("")
async def get_clients(client_id : str | None = None):
    if client_id:
        return Service.get_client_by_id_service(client_id)
    return Service.get_all_clients_service()

@router.delete("/delete")
async def delete_client(client_id: str):
    return Service.delete_client_by_id_service(client_id)

@router.post("/add")
async def add_client(client : Client):
    client_dict = client.dict()
    return Service.create_new_client(client_dict)

@router.put("/update")
async def update_client(client_id : str, new_data : Client):
    new_data_dict = new_data.dict()
    return Service.update_client(client_id, new_data_dict)