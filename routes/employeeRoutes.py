from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeModel import Employee

router = APIRouter(prefix="/Employees", tags=["Employees API"])

@router.get("")
async def get_employees(employee_id : str | None = None):
    if employee_id:
        if Service.getAllEmployee(employee_id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    else:
        if Service.getAllEmployee() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if employee_id:
            return Service.getAllEmployee(employee_id)
        return Service.getAllEmployee()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employee(employee_id: str):
    if Service.getById(employee_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    try:
        Service.DeleteById(employee_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("")
async def add_employee(employee : Employee):
    try:
        Service.createNew(employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("")
async def update_employee(employee_id : str, new_data : Employee):
    if Service.getById(employee_id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{employee_id}' not found")
    try:
        Service.updateById(employee_id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")