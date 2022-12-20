from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeModel import Employee

router = APIRouter(prefix="/Employees", tags=["Employees API"])

@router.get("")
async def get_employees(id : str | None = None):
    if id:
        if Service.get_employee_by_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    else:
        if Service.get_all_employees() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if id:
            return Service.get_employee_by_id(id)
        return Service.get_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employee(id: str):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.remove_employee_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("")
async def add_employee(employee : Employee):
    try:
        Service.create_employee(employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("")
async def update_employee(id : str, new_data : Employee):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.update_employee_by_id(id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")