from dao.companyDao import Company_dao
from models.companyModel import Company

class Company_dto:

    @classmethod
    def get_all(cls):
        companies = []
        results = Company_dao.find_all()
        for result in results:
                companies.append(Company(**result))
        return companies

    @classmethod
    def get_by_id(cls, id : str):
            result = Company_dao.find_by_id(id)
            return Company(**result[0])

    @classmethod
    def delete_by_id(cls, id : str):
        return Company_dao.remove_by_id(id)

    @classmethod
    def post(cls, item : Company):
        return Company_dao.create_new(item)
    
    @classmethod
    def put(cls, id : str, item : Company):
        return Company_dao.update_by_id(id, item)
