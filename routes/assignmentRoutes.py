from fastapi import APIRouter, HTTPException
from services.service import Service
from models.assignment import Assignment


router = APIRouter(prefix="/assignment", tags=["assignment"])

@router.get("")
async def get_all_assignments():
    req = Service.get_all_assignments_service()
    if req != None:
        return req
    elif req == None:
        raise HTTPException(status_code=404, detail="No assignments found")
    raise HTTPException(status_code=500 , detail="Something went wrong from our side, please try again later")

@router.get("/{id_commessa}")
async def get_assignment_by_id(id_commessa: str):
    req = Service.get_assignment_by_id_service(id_commessa)
    if req != None:
        return req
    elif req == None:
        raise HTTPException(status_code=404, detail="Assignment not found")
    raise HTTPException(status_code=500 , detail="Something went wrong from our side, please try again later")

@router.post("")
async def post_assignment(Assignment: Assignment):
    Service.post_assignment_service(Assignment)
    raise HTTPException(status_code=201, detail="Assignment created")
    

@router.put("/{id_commessa}")
async def put_assignment(id_commessa: str, Assignment: Assignment):
    req = Service.put_assignment_service(id_commessa, Assignment)
    if  Assignment.id_commessa == id_commessa:
        req
        raise HTTPException(status_code=201, detail="Assignment updated")
    elif req == None:
        raise HTTPException(status_code=404, detail="Assignment not found")
    raise HTTPException(status_code=500 , detail="Something went wrong from our side, please try again later")

@router.delete("/{id_commessa}")
async def delete_assignment(id_commessa: str):
    req = Service.delete_assignment_service(id_commessa)
    if id_commessa == id_commessa:
        req
        raise HTTPException(status_code=201, detail="Assignment deleted")
    elif req == None:
        raise HTTPException(status_code=404, detail="Assignment not found")
    raise HTTPException(status_code=500 , detail="Something went wrong from our side, please try again later")