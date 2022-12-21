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
        companies_clients = []
        results = CompanyClientDao.find_by_client_id(id)
        for result in results:
            companies_clients.append(CompanyClient(**result))
        return companies_clients

    @classmethod
    def get_by_company_id(cls, id : str):
        companies_clients = []
        results = CompanyClientDao.find_by_company_id(id)
        for result in results:
            companies_clients.append(CompanyClient(**result))
        return companies_clients

    @classmethod
    def get_specific(cls, id1 : str, id2 : str):
        result = CompanyClientDao.find_specific(id1, id2)
        return result

    @classmethod
    def delete_by_client_id(cls, id : str):
        return CompanyClientDao.remove_by_client_id(id)

    @classmethod
    def delete_by_company_id(cls, id : str):
        return CompanyClientDao.remove_by_company_id(id)

    @classmethod
    def delete_specific(cls, id1 : str, id2 : str):
        return CompanyClientDao.remove_specific(id1, id2)

    @classmethod
    def post(cls, item : CompanyClient):
        return CompanyClientDao.create(item)

    @classmethod
    def put(cls, id1 : str, id2 : str, item : CompanyClient):
        return CompanyClientDao.update(id1, id2, item)