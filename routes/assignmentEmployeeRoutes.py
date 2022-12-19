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
    
@router.get("/getById")
async def get_assignment_employee_by_id(filter: str, id: str):
    if filter == "assignment":
        if Service.get_assignments_employee_by_assignment_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Assignment with id: {id} not found")
        try:
            return Service.get_assignments_employee_by_assignment_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "employee":
        if Service.get_assignments_employee_by_employee_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Employee with id: {id} not found")
        try:
            return Service.get_assignments_employee_by_employee_id_service(id)
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
async def put_assignment_employee(filter: str, id: str, assignment_employee : AssignmentEmployee):
    if filter == "assignment":
        if Service.get_assignments_employee_by_assignment_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Assignment with id: {id} not found")
        try:
            Service.put_assignments_employee_by_assignment_id_service(id, assignment_employee)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "employee":
        if Service.get_assignments_employee_by_employee_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Employee with id: {id} not found")
        try:
            Service.put_assignments_employee_by_employee_id_service(id, assignment_employee)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=200, detail="Assignment Employee Updated Successfully")

@router.delete("")
async def delete_assignment_employee(filter: str, id: str):
    if filter == "assignment":
        if Service.get_assignments_employee_by_assignment_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Assignment with id: {id} not found")
        try:
            Service.delete_assignments_employee_by_assignment_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "employee":
        if Service.get_assignments_employee_by_employee_id_service(id) == None:
            raise HTTPException(status_code=404, detail=f"Employee with id: {id} not found")
        try:
            Service.delete_assignments_employee_by_employee_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=200, detail="Assignment Employee Deleted Successfully")