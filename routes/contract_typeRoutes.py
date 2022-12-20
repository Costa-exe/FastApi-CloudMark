from fastapi import APIRouter, HTTPException
from services.service import Service
from models.contract_typeModel import ContractType

router = APIRouter(prefix="/contract_types", tags=["Contract_types API"])

@router.get("")
async def get_contract_type():
    if Service.get_all_contract_type() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.get_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getByIdName")
async def get_by_id_name(filter : str, id : str):
    if filter == "id":
        if Service.get_contract_type_by_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contrato'='{id}' not found")
        try:
            return Service.get_contract_type_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.get__contract_type_by_name(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{id}' not found")
        try:
            return Service.get__contract_type_by_name(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_by_id_name(filter : str, id: str):
    if filter == "id":
        if Service.get_contract_type_by_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contratto'='{id}' not found")
        try:
            Service.remove_contract_type_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.get__contract_type_by_name(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_cliente'='{id}' not found")
        try:
            Service.remove_contract_type_by_name(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_company(filter : str , id : str, new_data : ContractType):
    if filter == "id":
        if Service.get_contract_type_by_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contratto'='{id}' not found")
        try:
            Service.update_contract_type_by_id(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.get__contract_type_by_name(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{id}' not found")
        try:
            Service.update_contract_type_by_name(id, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("")
async def add_company_client(contract_type : ContractType):
    try:
        Service.create_contract_type(contract_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")
