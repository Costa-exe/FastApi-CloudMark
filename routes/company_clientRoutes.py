from fastapi import APIRouter
from services.service import Service
from models.company_clientModel import Company_Client

router = APIRouter(prefix="/companies_clients", tags=["Companies_Clients API"])

@router.get("")
async def get_companies_clients():
    return Service.get_all_company_client_service()

@router.get("/getById")
async def get_company_client_by_id(filter : str, id : str):
    if filter == "client":
        return Service.get_company_client_by_client_id_service(id)
    elif filter == "company":
        return Service.get_company_client_by_company_id_service(id)

@router.delete("/delete")
async def delete_company_client_by_id(filter : str, id : str):
    if filter == "client":
        return Service.delete_company_client_by_client_id_service(id)
    elif filter == "company":
        return Service.delete_company_client_by_company_id_service(id)

@router.put("/put")
async def put_company(filter : str , id : str, new_data : Company_Client):
    if filter == "client":
        new_data_dict = new_data.dict()
        return Service.update_company_client_by_client_id(id, new_data_dict)
    elif filter == "company":
        new_data_dict = new_data.dict()
        return Service.update_company_client_by_company_id(id, new_data_dict)

@router.post("/add")
async def add_company_client(company_client : Company_Client):
    company_client_dict = company_client.dict()
    return Service.create_new_company_client(company_client_dict)