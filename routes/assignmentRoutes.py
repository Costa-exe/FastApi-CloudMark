from fastapi import APIRouter, HTTPException
from services.service import Service
from models.assignment import Assignment


router = APIRouter(prefix="/assignment", tags=["assignment"])

@router.get("")
async def get_assignments(id_commessa : str | None = None):
    if id_commessa:
        if Service.get_assignment_by_id_service(id_commessa) == None:
            raise HTTPException(status_code=404, detail=f"Commessa con id: {id_commessa} non trovata")
    else:
        if Service.get_all_assignments_service() == []:
            raise HTTPException(status_code=404, detail=f"Nessuna Commessa trovata")
    try:
        if id_commessa:
            return Assignment(**Service.get_assignment_by_id_service(id_commessa))
        return Service.get_all_assignments_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    
@router.post("")
async def post_assignment(assignment : Assignment):
    try:
        Service.post_assignment_service(assignment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Commessa creata con successo")

@router.put("")
async def put_assignment(id_commessa : str, assignment : Assignment):
    if Service.get_assignment_by_id_service(id_commessa) == None:
        raise HTTPException(status_code=404, detail=f"Commessa con id 'id_commessa'='{id_commessa}' non trovata")
    try:
        Service.put_assignment_service(id_commessa, assignment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Commessa aggiornata con successo")

@router.delete("")
async def delete_assignment(id_commessa: str):
    if Service.get_assignment_by_id_service(id_commessa) == None:
        raise HTTPException(status_code=404, detail=f"Commessa con id 'id_commessa'='{id_commessa}' non trovata")
    try:
        Service.delete_assignment_service(id_commessa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Commessa eliminata con successo")