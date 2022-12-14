from dto.companyDto import Company_dto

class Service:

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