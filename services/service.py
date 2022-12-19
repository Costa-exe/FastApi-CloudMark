from dto.companyDto import CompanyDto
from dto.clientDto import ClientDto
from dto.companyClientDto import CompanyClientDto
from models.clientModel import Client
from models.companyModel import Company
from models.companyClientModel import CompanyClient

class Service:

    #companies services

    @classmethod
    def get_all_companies_service(cls):
        return CompanyDto.get_all()

    @classmethod
    def get_company_by_id_service(cls, id : str):
        return CompanyDto.get_by_id(id)

    @classmethod
    def delete_company_by_id_service(cls, id : str):
        return CompanyDto.delete(id)

    @classmethod
    def create_new_company(cls, item : Company):
        return CompanyDto.post(item)

    @classmethod
    def update_company(cls, id : str, item : Company):
        return CompanyDto.put(id, item)

    #clients services    

    @classmethod
    def get_all_clients_service(cls):
        return ClientDto.get_all()

    @classmethod
    def get_client_by_id_service(cls, id : str):
        return ClientDto.get_by_id(id)

    @classmethod
    def delete_client_by_id_service(cls, id : str):
        return ClientDto.delete(id)

    @classmethod
    def create_new_client(cls, item : Client):
        return ClientDto.post(item)

    @classmethod
    def update_client(cls, id : str, item : Client):
        return ClientDto.put(id, item)

    #company_client services

    @classmethod
    def get_all_company_client_service(cls):
        return CompanyClientDto.get_all()

    @classmethod
    def get_company_client_by_client_id_service(cls, id : str):
        return CompanyClientDto.get_by_client_id(id)

    @classmethod
    def get_company_client_by_company_id_service(cls, id : str):
        return CompanyClientDto.get_by_company_id(id)

    @classmethod
    def delete_company_client_by_client_id_service(cls, id: str):
        return CompanyClientDto.delete_by_client_id(id)

    @classmethod
    def delete_company_client_by_company_id_service(cls, id : str):
        return CompanyClientDto.delete_by_company_id(id)

    @classmethod
    def create_new_company_client(cls, item : CompanyClient):
        return CompanyClientDto.post(item)

    @classmethod
    def update_company_client_by_client_id(cls, id : str, item : CompanyClient):
        return CompanyClientDto.put_by_client_id(id, item)
    
    @classmethod
    def update_company_client_by_company_id(cls, id : str, item : CompanyClient):
        return CompanyClientDto.put_by_company_id(id, item)


    