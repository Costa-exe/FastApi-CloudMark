from fastapi import APIRouter, HTTPException
from services.service import Service
from models.contract_typeModel import ContractType

router = APIRouter(prefix="/contract_types", tags=["Contract_types API"])

@router.get("")
async def get_contract_type():
    if Service.getAllEmployee() == []:
        raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        return Service.getAllEmployee()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.get("/getByIdName")
async def get_by_id_name(filter : str, id_tipo_contratto, nome_tipo_contratto : str):
    if filter == "id":
        if Service.getById(id_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contrato'='{id_tipo_contratto}' not found")
        try:
            return Service.getById(id_tipo_contratto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "name":
        if Service.getByName(nome_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{nome_tipo_contratto}' not found")
        try:
            return Service.getByName(nome_tipo_contratto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_by_id_name(filter : str, id_tipo_contratto, nome_tipo_contratto : str):
    if filter == "contract_id":
        if Service.getById(id_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contratto'='{id_tipo_contratto}' not found")
        try:
            Service.DeleteById(id_tipo_contratto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "contract_name":
        if Service.getByName(nome_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_cliente'='{nome_tipo_contratto}' not found")
        try:
            Service.DeleteByName(nome_tipo_contratto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.put("")
async def put_company(filter : str , id_tipo_contratto, nome_tipo_contratto : str, new_data : ContractType):
    if filter == "contract_id":
        if Service.getById(id_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_tipo_contratto'='{id_tipo_contratto}' not found")
        try:
            Service.updateById(id_tipo_contratto, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    elif filter == "contract_name":
        if Service.getByName(nome_tipo_contratto) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'nome_tipo_contratto'='{nome_tipo_contratto}' not found")
        try:
            Service.updateByName(nome_tipo_contratto, new_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")

@router.post("")
async def add_company_client(contract_type : ContractType):
    try:
        Service.createNew(contract_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")
