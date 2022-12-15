from fastapi import APIRouter
from services.service import Service
from models.companyModel import Company

router = APIRouter(prefix="/companies", tags=["Companies API"])

@router.get("")
async def get_companies(company_id : str | None = None):
    if company_id:
        return Service.get_company_by_id_service(company_id)
    return Service.get_all_companies_service()

@router.delete("/delete")
async def delete_company(company_id: str):
    return Service.delete_company_by_id_service(company_id)

@router.post("/add")
async def add_company(company : Company):
    return Service.create_new_company(company)

@router.put("/update")
async def update_company(company_id : str, new_data : Company):
    return Service.update_company(company_id, new_data)