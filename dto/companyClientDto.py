from dao.companyClientDao import CompanyClientDao
from models.companyClientModel import CompanyClient

class CompanyClientDto:

    @classmethod
    def get_all(cls):
        companies_clients = []
        results = CompanyClientDao.find_all()
        for result in results:
                companies_clients.append(CompanyClient(**result))
        return companies_clients

    @classmethod
    def get_by_client_id(cls, id : str):
        result = CompanyClientDao.find_by_client_id(id)
        return result

    @classmethod
    def get_by_company_id(cls, id : str):
        result = CompanyClientDao.find_by_company_id(id)
        return result

    @classmethod
    def delete_by_client_id(cls, id : str):
        return CompanyClientDao.remove_by_client_id(id)

    @classmethod
    def delete_by_company_id(cls, id : str):
        return CompanyClientDao.remove_by_company_id(id)

    @classmethod
    def post(cls, item : CompanyClient):
        return CompanyClientDao.create(item)

    @classmethod
    def put_by_client_id(cls, id : str, item : CompanyClient):
        return CompanyClientDao.update_by_client_id(id, item)
    
    @classmethod
    def put_by_company_id(cls, id : str, item : CompanyClient):
        return CompanyClientDao.update_by_company_id(id, item)