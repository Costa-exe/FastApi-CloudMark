from fastapi import APIRouter, HTTPException
from services.service import Service
from models.companyModel import Company

router = APIRouter(prefix="/companies", tags=["Companies API"])


@router.get("")
async def get_companies(id_azienda: str | None = None):
    if id_azienda:
        if Service.get_company_by_id_service(id_azienda) == None:
            raise HTTPException(
                status_code=404, detail=f"Azienda con id 'id_azienda'='{id_azienda}' non trovata")
    else:
        if Service.get_all_companies_service() == []:
            raise HTTPException(status_code=404, detail=f"Nessuna Azienda trovata")
    try:
        if id_azienda:
            return Company(**Service.get_company_by_id_service(id_azienda))
        return Service.get_all_companies_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.get("/getId")
async def get_id(nome: str):
    if Service.get_id_by_name(nome) == None:
        raise HTTPException(
            status_code=404, detail=f"Nessuna Azienda trovata")
    try:
        return Service.get_id_by_name(nome)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)


@router.delete("")
async def delete_company(id_azienda: str):
    if Service.get_company_by_id_service(id_azienda) == None:
        raise HTTPException(
            status_code=404, detail=f"Azienda con id 'id_azienda'='{id_azienda}' non trovata")
    try:
        Service.delete_company_by_id_service(id_azienda)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Azienda eliminata con successo")


@router.post("")
async def add_company(company: Company):
    try:
        Service.create_new_company(company)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Azienda aggiunta con successo")


@router.put("")
async def update_company(id_azienda: str, new_data: Company):
    if Service.get_company_by_id_service(id_azienda) == None:
        raise HTTPException(
            status_code=404, detail=f"Azienda con id 'id_azienda'='{id_azienda}' non trovata")
    try:
        Service.update_company(id_azienda, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Azienda aggiornata con successo")
