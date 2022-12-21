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
            return Service.get_employee_company_by_employee_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "company":
        if Service.get_employee_company_by_company_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_azienda'='{id}' not found")
        try:
            return Service.get_employee_company_by_company_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getSpecific")
async def get_specific_employees_companies(id_dipendente : str, id_azienda : str):
    if Service.get_specific_contract_type_service(id_dipendente, id_azienda) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_dipendente'='{id_dipendente}' and 'id_azienda'='{id_azienda}' not found")
    try:
        return EmployeeCompany(**Service.get_specific_contract_type_service(id_dipendente, id_azienda))
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

@router.delete("/deleteSpecific")
async def delete_specific_employee_company(id_dipendente : str, id_azienda : str):
    if Service.get_specific_employee_company_service(id_dipendente, id_azienda) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_dipendente'='{id_dipendente}' and 'id_azienda'='{id_azienda}' not found")
    try:
        Service.delete_specific_employee_company_service(id_dipendente, id_azienda)
    except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_employee_company(id_dipendente: str, id_azienda : str, new_data : EmployeeCompany):
    if Service.get_specific_employee_company_service(id_dipendente, id_azienda) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_dipendente'='{id_dipendente}' and 'id_azienda'='{id_azienda}' not found")
    try:
        Service.update_employee_company_service(id_dipendente, id_azienda, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")


@router.post("")
async def add__employee_company(employee_company : EmployeeCompany):
    try:
        Service.create_employee_company(employee_company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")