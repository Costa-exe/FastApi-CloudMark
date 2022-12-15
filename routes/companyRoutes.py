from fastapi import APIRouter, HTTPException
from services.service import Service
from models.companyModel import Company

router = APIRouter(prefix="/companies", tags=["Companies API"])

@router.get("")
async def get_companies(company_id : str | None = None):
    if company_id:
        if Service.get_company_by_id_service(company_id) == None:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            return Service.get_company_by_id_service(company_id)
    return Service.get_all_companies_service()

@router.delete("/delete")
async def delete_company(company_id: str):
    return Service.delete_company_by_id_service(company_id)

@router.post("/add")
async def add_company(company : Company):
    try:
        Service.create_new_company(company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=200, detail="Item Added Successfully")

@router.put("/update")
async def update_company(company_id : str, new_data : Company):
    return Service.update_company(company_id, new_data)