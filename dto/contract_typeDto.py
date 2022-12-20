from dao.contract_typeDao import ContractTypeDao
from models.contract_typeModel import ContractType

class ContractTypeDto:

    @classmethod
    def get_all(cls):
        ContractType = []
        results = ContractTypeDao.find_all()
        for result in results:
                ContractType.append(result)
        return ContractType

    @classmethod
    def get_by_id(cls, id_tipo_contratto : str):
        result = ContractTypeDao.find_by_id(id_tipo_contratto)
        return result

    @classmethod
    def get_by_name(cls, nome_tipo_contratto : str):
        result = ContractTypeDao.find_by_name(nome_tipo_contratto)
        return result


    @classmethod
    def delete_by_id(cls, id_tipo_contratto : str):
        return ContractTypeDao.remove_by_id(id_tipo_contratto)

    @classmethod
    def delete_by_name(cls, nome_tipo_contratto : str):
        return ContractTypeDao.remove_by_name(nome_tipo_contratto)

    @classmethod
    def put(cls, id_tipo_contratto : str, item : ContractType):
        return ContractTypeDao.update_by_id(id_tipo_contratto, item)

    @classmethod
    def put(cls, nome_tipo_contratto :str, item: ContractType):
        return ContractTypeDao.update_by_name(nome_tipo_contratto, item)

    @classmethod
    def post(cls, item : ContractType):
        return ContractTypeDao.create(item)