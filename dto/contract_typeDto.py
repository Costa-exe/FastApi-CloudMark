from dao.contract_typeDao import Contract_typeDao
from models.contract_typeModel import ContractType

class ContractTypeDto:

    @classmethod
    def getAllEmployee(cls):
        ContractType = []
        results = Contract_typeDao.findAll()
        for result in results:
                ContractType.append(ContractType(**result))
        return ContractType

    @classmethod
    def getById(cls, id_tipo_contratto : str):
        result = Contract_typeDao.findById(id_tipo_contratto)
        return ContractType(**result[0])

    @classmethod
    def getByName(cls, nome_tipo_contratto : str):
        result = Contract_typeDao.findByName(nome_tipo_contratto)
        return ContractType(**result[0])


    @classmethod
    def DeleteById(cls, id_tipo_contratto : str):
        return Contract_typeDao.removeById(id_tipo_contratto)

    @classmethod
    def DeleteByName(cls, nome_tipo_contratto : str):
        return Contract_typeDao.removeById(nome_tipo_contratto)

    @classmethod
    def put(cls, id_tipo_contratto, item):
        return Contract_typeDao.updateById(id_tipo_contratto, item)

    @classmethod
    def put(cls, nome_tipo_contratto, item):
        return Contract_typeDao.updateByName(nome_tipo_contratto, item)

    @classmethod
    def post(cls, item):
        return Contract_typeDao.createNew(item)