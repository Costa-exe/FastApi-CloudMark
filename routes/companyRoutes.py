from fastapi import APIRouter, HTTPException
from services.service import Service
from models.companyModel import Company

router = APIRouter(prefix="/companies", tags=["Companies API"])

@router.get("")
async def get_companies(company_id : str | None = None):
    if company_id:
        if Service.get_company_by_id_service(company_id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{company_id}' not found")
    else:
        if Service.get_all_companies_service() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if company_id:
            return Service.get_company_by_id_service(company_id)
        return Service.get_all_companies_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("/delete")
async def delete_company(company_id: str):
    if Service.get_company_by_id_service(company_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{company_id}' not found")
    try:
        Service.delete_company_by_id_service(company_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("/add")
async def add_company(company : Company):
    try:
        Service.create_new_company(company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("/update")
async def update_company(company_id : str, new_data : Company):
    if Service.get_company_by_id_service(company_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{company_id}' not found")
    try:
        Service.update_company(company_id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")