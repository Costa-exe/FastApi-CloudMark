from fastapi import APIRouter, HTTPException
from services.service import Service
from models.clientModel import Client

router = APIRouter(prefix="/clients", tags=["Clients API"])

@router.get("")
async def get_clients(id_cliente : str | None = None):
    if id_cliente:
        if Service.get_client_by_id_service(id_cliente) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    else:
        if Service.get_all_clients_service() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if id_cliente:
            return Client(**Service.get_client_by_id_service(id_cliente))
        return Service.get_all_clients_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/AssignmentDetails")
async def get_assignments_details(id_commessa : str):
    if Service.get_assignment_details(id_commessa) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_commessa'='{id_commessa}' not found")
    try:
        return Service.get_assignment_details(id_commessa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getActiveByName")
async def get_active_by_name(nome : str):
    if Service.get_active_clients_by_name(nome) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients_by_name(nome)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getActiveByVat")
async def get_active_by_vat(p_iva: str):
    if Service.get_active_clients_by_vat(p_iva) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients_by_vat(p_iva)
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

@router.get("/getAllActive")
async def get_all_active():
    if Service.get_all_active_clients() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all_active_clients()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getActiveDetailsByVat")
async def get_active_details_by_vat(p_iva: str):
    if Service.get_active_clients_details_by_vat(p_iva) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients_details_by_vat(p_iva)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getActiveDetailsByName")
async def get_active_details_by_name(name: str):
    if Service.get_active_clients_details_by_name(name) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_active_clients_details_by_name(name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_client(id_cliente: str):
    if Service.get_client_by_id_service(id_cliente) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    try:
        Service.delete_client_by_id_service(id_cliente)
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
async def update_client(id_cliente : str, new_data : Client):
    if Service.get_client_by_id_service(id_cliente) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id_cliente}' not found")
    try:
        Service.update_client(id_cliente, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")