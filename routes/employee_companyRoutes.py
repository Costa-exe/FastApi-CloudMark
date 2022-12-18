from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employee_companyModel import EmployeeCompany

router = APIRouter(prefix="/employees_companies", tags=["Employees_Companies API"])

@router.get("")
async def get_employees_companies():
    if Service.getAllEmployee_company() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.getAllEmployee_company()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getById")
async def get_employees_companies_by_id(filter : str, id_dipendente, id_azienda : str):
    if filter == "employee":
        if Service.getEmployeeId(id_dipendente) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id_dipendente}' not found")
        try:
            return Service.getEmployeeId(id_dipendente)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.getCompanyId(id_azienda) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id_azienda}' not found")
        try:
            return Service.getCompanyId(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employees_company_by_id(filter : str, id_dipendente, id_azienda : str):
    if filter == "employee":
        if Service.getEmployeeId(id_dipendente) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id_dipendente}' not found")
        try:
            Service.DeleteByEmployeeId(id_dipendente)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.getCompanyId(id_azienda) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id_azienda}' not found")
        try:
            Service.DeleteByCompanyId(id_azienda)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put__employee_company(filter : str , id_dipendente, id_azienda : str, new_data : EmployeeCompany):
    if filter == "employee":
        if Service.getEmployeeId(id_dipendente) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id_dipendente}' not found")
        try:
            Service.updateByEmployeeId(id_dipendente, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.getCompanyId(id_azienda) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id_azienda}' not found")
        try:
            Service.updateByCompanyId(id_azienda, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("")
async def add__employee_company(employee_company : EmployeeCompany):
    try:
        Service.createNew(employee_company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")