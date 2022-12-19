from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeModel import Employee

router = APIRouter(prefix="/Employees", tags=["Employees API"])

@router.get("")
async def get_employees(employee_id : str | None = None):
    if employee_id:
        if Service.get_all(employee_id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    else:
        if Service.get_all() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if employee_id:
            return Service.get_all(employee_id)
        return Service.get_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employee(employee_id: str):
    if Service.get_by_id(employee_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    try:
        Service.remove_by_id(employee_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("")
async def add_employee(employee_id : Employee):
    try:
        Service.create(employee_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("")
async def update_employee(employee_id : str, new_data : Employee):
    if Service.get_by_id(employee_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    try:
        Service.update_by_id(employee_id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")