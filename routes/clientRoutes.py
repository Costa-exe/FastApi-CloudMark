from fastapi import APIRouter, HTTPException
from services.service import Service
from models.clientModel import Client
from starlette.responses import FileResponse
from models.customClientModel import CustomClient

router = APIRouter(prefix="/clients", tags=["Clients API"])


@router.get("")
async def get_clients(id_cliente: str | None = None):
    if id_cliente:
        if Service.get_client_by_id_service(id_cliente) == None:
            raise HTTPException(
                status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    else:
        if Service.get_all_clients_service() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if id_cliente:
            return Client(**Service.get_client_by_id_service(id_cliente))
        return Service.get_all_clients_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.post("/getCsv")
async def get_clients_csv(clients: list[CustomClient]):
    try:
        return Service.get_clients_csv(clients)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/downloadCsv")
async def download_csv():
    try:
        file_path = "./clienti.csv"
        return FileResponse(path=file_path, media_type='text/csv', filename=file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/deleteCsv")
async def remove_csv():
    try:
        return Service.remove_clients_csv()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/AssignmentDetails")
async def get_assignments_details(id_commessa: str):
    if Service.get_assignment_details(id_commessa) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_commessa'='{id_commessa}' not found")
    try:
        return Service.get_assignment_details(id_commessa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getByNameVat")
async def get_active_clients(value: str, id_azienda: str):
    if Service.get_active_clients(value, id_azienda) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients(value, id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getActiveAssignments")
async def get_active_assignments(p_iva: str):
    if Service.get_active_assignments(p_iva) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_assignments(p_iva)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getAll")
async def get_all_active(id_azienda: str):
    if Service.get_all_active_clients(id_azienda) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all_active_clients(id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getByNameVatDetails")
async def get_active_details(value: str, id_azienda: str):
    if Service.get_active_clients_details(value, id_azienda) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients_details(value, id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.delete("")
async def delete_client(id_cliente: str):
    if Service.get_client_by_id_service(id_cliente) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    try:
        Service.delete_client_by_id_service(id_cliente)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")


@router.post("")
async def add_client(client: Client):
    try:
        Service.create_new_client(client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")


@router.put("")
async def update_client(id_cliente: str, new_data: Client):
    if Service.get_client_by_id_service(id_cliente) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    try:
        Service.update_client(id_cliente, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")
