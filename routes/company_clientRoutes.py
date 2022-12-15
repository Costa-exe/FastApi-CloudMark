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
        in_db_comapny_client = Service.get_company_client_by_client_id_service(id)
        in_db_comapny_client_model = Company_Client(**in_db_comapny_client())
        db_data_to_patch = new_data.dict(exclude_unset=True)
        patched_db = in_db_comapny_client_model.copy(update=db_data_to_patch)
        return Service.update_company_client_by_client_id(id, patched_db.dict())
    elif filter == "company":
        in_db_comapny_client = Service.get_company_client_by_company_id_service(id)
        in_db_comapny_client_model = Company_Client(**in_db_comapny_client())
        db_data_to_patch = new_data.dict(exclude_unset=True)
        patched_db = in_db_comapny_client_model.copy(update=db_data_to_patch)
        return Service.update_company_client_by_company_id(id, patched_db.dict())