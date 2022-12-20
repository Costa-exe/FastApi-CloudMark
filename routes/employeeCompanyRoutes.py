from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeCompanyModel import EmployeeCompany

router = APIRouter(prefix="/employees_companies", tags=["Employees_Companies API"])

@router.get("")
async def get_employees_companies():
    if Service.get_all_employee_company() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all_employee_company()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getById")
async def get_employees_companies_by_id(filter : str, id : str):
    if filter == "employee":
        if Service.get_employee_company_by_employee_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
        try:
            return EmployeeCompany(**Service.get_employee_company_by_employee_id(id))
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_employee_company_by_company_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id}' not found")
        try:
            return EmployeeCompany(**Service.get_employee_company_by_company_id(id))
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employees_company_by_id(filter : str, id : str):
    if filter == "employee":
        if Service.get_employee_company_by_employee_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
        try:
            Service.remove_employee_company_by_employee_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_employee_company_by_company_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id}' not found")
        try:
            Service.remove_employee_company_by_company_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_employee_company(filter : str , id : str, new_data : EmployeeCompany):
    if filter == "employee":
        if Service.get_employee_company_by_employee_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
        try:
            Service.update_employee_company_by_employee_id(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_employee_company_by_company_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id}' not found")
        try:
            Service.update_employee_company_by_company_id(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("")
async def add_employee_company(employee_company : EmployeeCompany):
    try:
        Service.create_employee_company(employee_company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")