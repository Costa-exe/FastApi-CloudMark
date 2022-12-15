from dto.companyDto import Company_dto
from dto.clientDto import Client_dto
from dto.company_clientDto import Company_Client_dto

class Service:

    #companies services

    @classmethod
    def get_all_companies_service(cls):
        return Company_dto.get_all()

    @classmethod
    def get_company_by_id_service(cls, id : str):
        return Company_dto.get_by_id(id)

    @classmethod
    def delete_company_by_id_service(cls, id: str):
        return Company_dto.delete_by_id(id)

    @classmethod
    def create_new_company(cls, item):
        return Company_dto.post(item)

    @classmethod
    def update_company(cls, id, item):
        return Company_dto.put(id, item)

    #clients services    

    @classmethod
    def get_all_clients_service(cls):
        return Client_dto.get_all()

    @classmethod
    def get_client_by_id_service(cls, id : str):
        return Client_dto.get_by_id(id)

    @classmethod
    def delete_client_by_id_service(cls, id: str):
        return Client_dto.delete_by_id(id)

    @classmethod
    def create_new_client(cls, item):
        return Client_dto.post(item)

    @classmethod
    def update_client(cls, id, item):
        return Client_dto.put(id, item)

    #company_client services

    @classmethod
    def get_all_company_client_service(cls):
        return Company_Client_dto.get_all()

    @classmethod
    def get_company_client_by_client_id_service(cls, id : str):
        return Company_Client_dto.get_by_client_id(id)

    @classmethod
    def get_company_client_by_company_id_service(cls, id : str):
        return Company_Client_dto.get_by_company_id(id)

    @classmethod
    def delete_comapny_client_by_client_id_service(cls, id: str):
        return Company_Client_dto.delete_by_client_id(id)

    @classmethod
    def delete_comapny_client_by_comapany_id_service(cls, id: str):
        return Company_Client_dto.delete_by_company_id(id)

    @classmethod
    def create_new_company_client(cls, item):
        return Company_Client_dto.post(item)

    @classmethod
    def update_comapny_client_by_client_id(cls, id, item):
        return Company_Client_dto.put_by_client_id(id, item)
    
    @classmethod
    def update_comapny_company_by_client_id(cls, id, item):
        return Company_Client_dto.put_by_company_id(id, item)


    