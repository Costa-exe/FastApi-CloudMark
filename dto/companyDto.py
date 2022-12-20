from dao.companyDao import CompanyDao
from models.companyModel import Company

class CompanyDto:

    @classmethod
    def get_all(cls):
        companies = []
        results = CompanyDao.find_all()
        for result in results:
                companies.append(Company(**result))
        return companies

    @classmethod
    def get_by_id(cls, id : str):
            result = CompanyDao.find_by_id(id)
            return Company(**result)

    @classmethod
    def delete(cls, id : str):
        return CompanyDao.remove_by_id(id)

    @classmethod
    def post(cls, item : Company):
        return CompanyDao.create(item)
    
    @classmethod
    def put(cls, id : str, item : Company):
        return CompanyDao.update_by_id(id, item)
