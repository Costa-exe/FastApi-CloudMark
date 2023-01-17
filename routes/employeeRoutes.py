from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeModel import Employee
from models.employeeCompanyModel import EmployeeCompany
import csv
from models.customEmployeeModel import CustomEmployee
from starlette.responses import FileResponse

router = APIRouter(prefix="/employees", tags=["Employees API"])


@router.get("")
async def get_employees(id: str | None = None):
    if id:
        if Service.get_employee_by_id(id) == None:
            raise HTTPException(
                status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    else:
        if Service.get_all_employees() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if id:
            return Employee(**Service.get_employee_by_id(id))
        return Service.get_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getByNameSurname")
async def get_by_name_surname(nome_cognome: str):
    if Service.get_employees_by_name_surname(nome_cognome) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_employees_by_name_surname(nome_cognome)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getByMultiFields")
async def get_by_multi(value: str, id_azienda: str):
    if Service.get_employees_by_multi(value, id_azienda) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_employees_by_multi(value, id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getByMultiFieldsActive")
async def get_by_multi(value: str, id_azienda: str):
    if Service.get_employees_by_multi_active(value, id_azienda) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_employees_by_multi_active(value, id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getAll")
async def get_all(working: str, id_azienda: str):
    if working == "no":
        if Service.get_employees_inactive(id_azienda) == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    elif working == "yes":
        if Service.get_employees_active(id_azienda) == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if working == "no":
            return Service.get_employees_inactive(id_azienda)
        return Service.get_employees_active(id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getFullDetails")
async def get_full_details(id_dipendente: str):
    if Service.get_employees_full_details(id_dipendente) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_dipendente'='{id_dipendente}' not found")
    try:
        return Service.get_employees_full_details(id_dipendente)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.post("/getCsv")
async def get_employees_csv(employees: list[CustomEmployee]):
    try:
        return Service.get_employees_csv(employees)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/downloadCsv")
async def download_csv():
    try:
        file_path = "./dipendenti.csv"
        return FileResponse(path=file_path, media_type='text/csv', filename=file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/getInfoAssignments")
async def get_info_assignments(id_dipendente: str):
    if Service.get_employees_info_assignments(id_dipendente) == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_employees_info_assignments(id_dipendente)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.delete("")
async def delete_employee(id: str):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.remove_employee_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")


@router.post("")
async def add_employee(employee: Employee):
    try:
        Service.create_employee(employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")


@router.post("/insertEmployeeCompany")
async def add_employee_company(employee: Employee, employeeCompany: EmployeeCompany):
    try:
        Service.create_employee(employee)
        Service.create_employee_company(employeeCompany)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")


@router.put("")
async def update_employee(id: str, new_data: Employee):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(
            status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.update_employee_by_id(id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")
