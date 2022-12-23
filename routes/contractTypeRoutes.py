from fastapi import APIRouter, HTTPException
from services.service import Service
from models.contractTypeModel import ContractType

router = APIRouter(prefix="/contract_types", tags=["Contract_types API"])

@router.get("")
async def get_contract_type():
    if Service.get_all_contract_type_service() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all_contract_type_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getByIdName")
async def get_by_id_name(filter : str, id : str):
    if filter == "id":
        if Service.get_contract_type_by_id(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contrato'='{id}' not found")
        try:
            return Service.get_contract_type_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.get_contract_type_by_name(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{id}' not found")
        try:
            return Service.get_contract_type_by_name(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getSpecific")
async def get_specific_contract_type(id_tipo_contratto : str, nome_tipo_contratto : str):
    if Service.get_specific_contract_type_service(id_tipo_contratto, nome_tipo_contratto) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_tipo_contratto'='{id_tipo_contratto}' and 'nome_tipo_contratto'='{nome_tipo_contratto}' not found")
    try:
        return ContractType(**Service.get_specific_contract_type_service(id_tipo_contratto, nome_tipo_contratto))
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)    

@router.delete("/deleteById")
async def delete_by_id_name(filter : str, id: str):
    if filter == "id":
        if Service.get_contract_type_by_id(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contratto'='{id}' not found")
        try:
            Service.delete_contract_type_by_id_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.get_contract_type_by_name(id) == []:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{id}' not found")
        try:
            Service.delete_contract_type_by_name_service(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.delete("/deleteSpecific")
async def delete_specific_contract_type(id_tipo_contratto : str, nome_tipo_contratto : str):
    if Service.get_specific_contract_type_service(id_tipo_contratto, nome_tipo_contratto) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_tipo_contratto'='{id_tipo_contratto}' and 'nome_tipo_contratto'='{nome_tipo_contratto}' not found")
    try:
        Service.delete_specific_contract_type_service(id_tipo_contratto, nome_tipo_contratto)
    except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_contract_type(id_tipo_contratto: str, nome_tipo_contratto : str, new_data : ContractType):
    if Service.get_specific_contract_type_service(id_tipo_contratto, nome_tipo_contratto) == None:
        raise HTTPException(status_code=404, detail=f"Item with keys 'id_tipo_contratto'='{id_tipo_contratto}' and 'nome_tipo_contratto'='{nome_tipo_contratto}' not found")
    try:
        Service.update_contract_type_service(id_tipo_contratto, nome_tipo_contratto, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")


@router.post("")
async def add_contract_type(contract_type : ContractType):
    try:
        Service.create_new_contract_type_service(contract_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")
