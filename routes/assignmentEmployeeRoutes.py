from fastapi import APIRouter, HTTPException
from services.service import Service
from models.assignmentEmployee import AssignmentEmployee

router = APIRouter(prefix="/assignment-employee", tags=["assignment-employee"]) 

@router.get("")
async def get_assignments_emploies():
    if Service.get_all_assignments_employee_service() == []:
        raise HTTPException(status_code=404, detail=f"No Assignments found")
    try:
        return Service.get_all_assignments_employee_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    
@router.get("/getSpecific")
async def get_specific_company_client(id_commessa : str, id_dipendente : str):
    if Service.get_specific_assignments_employee(id_commessa, id_dipendente) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_commessa'='{id_commessa}' and 'id_dipendente'='{id_dipendente}' not found")
    try:
        return AssignmentEmployee(**Service.get_specific_assignments_employee(id_commessa, id_dipendente))
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    
@router.get("/getById")
async def get_assignment_employee_by_id(filter: str, id: str):
    if filter == "assignment":
        if Service.get_assignments_employee_by_assignment_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Assignment with id: {id} not found")
        try:
            return AssignmentEmployee(**Service.get_assignments_employee_by_assignment_id_service(id))
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "employee":
        if Service.get_assignments_employee_by_employee_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Employee with id: {id} not found")
        try:
            return AssignmentEmployee(**Service.get_assignments_employee_by_employee_id_service(id))
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
        
@router.post("")
async def post_assignment_employee(assignment_employee : AssignmentEmployee):
    try:
        Service.post_assignments_employee_service(assignment_employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Assignment Employee Created Successfully")

@router.put("")
async def put_assignment_employee(id_commessa : str, id_dipendente : str, new_data : AssignmentEmployee):
    if Service.get_specific_assignments_employee(id_commessa, id_dipendente) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_commessa'='{id_commessa}' and 'id_dipendente'='{id_dipendente}' not found")
    try:
        Service.put_assignments_employee_service(id_commessa, id_dipendente, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.delete("")
async def delete_assignment_employee(filter: str, id: str):
    if filter == "assignment":
        if Service.get_assignments_employee_by_assignment_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Assignment with id: {id} not found")
        try:
            Service.delete_assignments_employee_by_assignment_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "employee":
        if Service.get_assignments_employee_by_employee_id_service(id) == []:
            raise HTTPException(status_code=404, detail=f"Employee with id: {id} not found")
        try:
            Service.delete_assignments_employee_by_employee_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=200, detail="Assignment Employee Deleted Successfully")

@router.delete("/deleteSpecific")
async def delete_specific_assignment_employee(id_commessa : str, id_dipendente : str):
    if Service.get_specific_assignments_employee(id_commessa, id_dipendente) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_commessa'='{id_commessa}' and 'id_dipendente'='{id_dipendente}' not found")
    try:
        Service.delete_specific_assignments_employee(id_commessa, id_dipendente)
    except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")