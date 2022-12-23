from fastapi import APIRouter, HTTPException
from services.service import Service
from models.companyClientModel import CompanyClient

router = APIRouter(prefix="/companies_clients", tags=["Companies_Clients API"])

@router.get("")
async def get_companies_clients():
    if Service.get_all_company_client_service() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all_company_client_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getById")
async def get_company_client_by_id(filter : str, id : str):
    if filter == "client":
        if Service.get_company_client_by_client_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            return Service.get_company_client_by_client_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_company_client_by_company_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id}' not found")
        try:
            return Service.get_company_client_by_company_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getSpecific")
async def get_specific_company_client(id_azienda : str, id_cliente : str):
    if Service.get_specific_company_client_service(id_azienda, id_cliente) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_azienda'='{id_azienda}' and 'id_cliente'='{id_cliente}' not found")
    try:
        return CompanyClient(**Service.get_specific_company_client_service(id_azienda, id_cliente))
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)    

@router.delete("/deleteById")
async def delete_company_client_by_id(filter : str, id : str):
    if filter == "client":
        if Service.get_company_client_by_client_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"No items with key 'id_cliente'='{id}' not found")
        try:
            Service.delete_company_client_by_client_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_company_client_by_company_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"No items with key 'id_azienda'='{id}' not found")
        try:
            Service.delete_company_client_by_company_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Items Deleted Successfully")

@router.delete("/deleteSpecific")
async def delete_specific_company_client(id_azienda : str, id_cliente : str):
    if Service.get_specific_company_client_service(id_azienda, id_cliente) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_azienda'='{id_azienda}' and 'id_cliente'='{id_cliente}' not found")
    try:
        Service.delete_specific_company_client_service(id_azienda, id_cliente)
    except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_company_client(id_azienda : str, id_cliente : str, new_data : CompanyClient):
    if Service.get_specific_company_client_service(id_azienda, id_cliente) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_azienda'='{id_azienda}' and 'id_cliente'='{id_cliente}' not found")
    try:
        Service.update_company_client_service(id_azienda, id_cliente, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("")
async def add_company_client(company_client : CompanyClient):
    try:
        Service.create_new_company_client_service(company_client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")