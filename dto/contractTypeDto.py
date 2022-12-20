from dao.contractTypeDao import ContractTypeDao
from models.contractTypeModel import ContractType

class ContractTypeDto:

    @classmethod
    def get_all(cls):
        ContractType = []
        results = ContractTypeDao.find_all()
        for result in results:
                ContractType.append(result)
        return ContractType

    @classmethod
    def get_by_id(cls, id : str):
        result = ContractTypeDao.find_by_id(id)
        return result

    @classmethod
    def get_by_name(cls, name : str):
        result = ContractTypeDao.find_by_name(name)
        return result


    @classmethod
    def delete_by_id(cls, id : str):
        return ContractTypeDao.remove_by_id(id)

    @classmethod
    def delete_by_name(cls, name : str):
        return ContractTypeDao.remove_by_name(name)

    @classmethod
    def put_by_id(cls, id : str, item : ContractType):
        return ContractTypeDao.update_by_id(id, item)

    @classmethod
    def put_by_name(cls, name :str, item: ContractType):
        return ContractTypeDao.update_by_name(name, item)

    @classmethod
    def post(cls, item : ContractType):
        return ContractTypeDao.create(item)