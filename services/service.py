from dto.companyDto import Company_dto

class Service:

    @classmethod
    def get_all_service(cls):
        return Company_dto.get_all()

    @classmethod
    def get_by_id_service(cls):
        return Company_dto.get_by_id()