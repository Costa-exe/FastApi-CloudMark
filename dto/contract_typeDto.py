from dao.contract_typeDao import ContractTypeDao
from models.contract_typeModel import ContractType

class ContractTypeDto:

    @classmethod
    def getAllEmployee(cls):
        ContractType = []
        results = ContractTypeDao.findAll()
        for result in results:
                ContractType.append(result)
        return ContractType

    @classmethod
    def getById(cls, id_tipo_contratto : str):
        result = ContractTypeDao.findById(id_tipo_contratto)
        return result

    @classmethod
    def getByName(cls, nome_tipo_contratto : str):
        result = ContractTypeDao.findByName(nome_tipo_contratto)
        return result


    @classmethod
    def DeleteById(cls, id_tipo_contratto : str):
        return ContractTypeDao.removeById(id_tipo_contratto)

    @classmethod
    def DeleteByName(cls, nome_tipo_contratto : str):
        return ContractTypeDao.removeById(nome_tipo_contratto)

    @classmethod
    def put(cls, id_tipo_contratto : str, item : ContractType):
        return ContractTypeDao.updateById(id_tipo_contratto, item)

    @classmethod
    def put(cls, nome_tipo_contratto :str, item: ContractType):
        return ContractTypeDao.updateByName(nome_tipo_contratto, item)

    @classmethod
    def post(cls, item : ContractType):
        return ContractTypeDao.createNew(item)