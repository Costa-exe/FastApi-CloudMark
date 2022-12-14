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
    company_dict = company.dict()
    return Service.create_new_company(company_dict)

@router.put("/update")
async def update_company(company_id : str, new_data : Company):
    new_data_dict = new_data.dict()
    return Service.update_company(company_id, new_data_dict)

@router.patch("/patch")
async def patch_company(company_id : str, new_data : Company):
    in_db_company = Service.get_company_by_id_service(company_id)
    in_db_company_model = Company(**in_db_company.dict())
    db_data_to_patch = new_data.dict(exclude_unset=True)
    patched_db = in_db_company_model.copy(update=db_data_to_patch)
    return Service.update_company(company_id, patched_db.dict())