from fastapi import APIRouter, HTTPException
from services.service import Service
from models.clientModel import Client

router = APIRouter(prefix="/clients", tags=["Clients API"])

@router.get("")
async def get_clients(client_id : str | None = None):
    if client_id:
        if Service.get_client_by_id_service(client_id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{client_id}' not found")
    else:
        if Service.get_all_clients_service() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if client_id:
            return Service.get_client_by_id_service(client_id)
        return Service.get_all_clients_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_client(client_id: str):
    if Service.get_client_by_id_service(client_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{client_id}' not found")
    try:
        Service.delete_client_by_id_service(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("")
async def add_client(client : Client):
    try:
        Service.create_new_client(client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("")
async def update_client(client_id : str, new_data : Client):
    if Service.get_client_by_id_service(client_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{client_id}' not found")
    try:
        Service.update_client(client_id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")