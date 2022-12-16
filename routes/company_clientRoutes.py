from fastapi import APIRouter, HTTPException
from services.service import Service
from models.company_clientModel import Company_Client

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
        if Service.get_company_client_by_client_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            return Service.get_company_client_by_client_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_company_client_by_company_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            return Service.get_company_client_by_company_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.delete("/delete")
async def delete_company_client_by_id(filter : str, id : str):
    if filter == "client":
        if Service.get_company_client_by_client_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            Service.delete_company_client_by_client_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_company_client_by_company_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            Service.delete_company_client_by_company_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("/put")
async def put_company(filter : str , id : str, new_data : Company_Client):
    if filter == "client":
        if Service.get_company_client_by_client_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            Service.update_company_client_by_client_id(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_company_client_by_company_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_cliente'='{id}' not found")
        try:
            Service.update_company_client_by_company_id(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("/add")
async def add_company_client(company_client : Company_Client):
    try:
        Service.create_new_company_client(company_client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")