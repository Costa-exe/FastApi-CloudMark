from dao.company_clientDao import Company_Client_dao
from models.company_clientModel import Company_Client

class Company_Client_dto:

    @classmethod
    def get_all(cls):
        companies_clients = []
        results = Company_Client_dao.find_all()
        for result in results:
                companies_clients.append(Company_Client(**result))
        return companies_clients

    @classmethod
    def get_by_client_id(cls, id : str):
        result = Company_Client_dao.find_by_client_id(id)
        return Company_Client(**result[0])

    @classmethod
    def get_by_company_id(cls, id : str):
        result = Company_Client_dao.find_by_company_id(id)
        return Company_Client(**result[0])

    @classmethod
    def delete_by_client_id(cls, id : str):
        return Company_Client_dao.remove_by_client_id(id)

    @classmethod
    def delete_by_company_id(cls, id : str):
        return Company_Client_dao.remove_by_company_id(id)

    @classmethod
    def post(cls, item):
        return Company_Client_dao.create_new(item)

    @classmethod
    def put_by_client_id(cls, id, item):
        return Company_Client_dao.update_by_client_id(id, item)
    
    @classmethod
    def put_by_company_id(cls, id, item):
        return Company_Client_dao.update_by_company_id(id, item)