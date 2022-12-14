from dao.companyDao import Company_dao

class Company:
    
    def __init__(self, id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        self.id_azienda = id_azienda
        self.nome = nome
        self.p_iva = p_iva
        self.indirizzo = indirizzo
        self.cap = cap
        self.iban = iban
        self.telefono = telefono
        self.email = email
        self.pec = pec
        self.fax = fax

class Company_dto:

    @classmethod
    def get_all(cls):
        companies = []
        results = Company_dao.find_all()
        for result in results:
                companies.append(Company(*result))
        return companies

    @classmethod
    def get_by_id(cls, id : str):
        result = Company_dao.find_by_id(id)
        return Company(*result[0])

    @classmethod
    def delete_by_id(cls, id : str):
        return Company_dao.remove_by_id(id)

    @classmethod
    def post(cls, item):
        return Company_dao.create_new(item)
    
    @classmethod
    def put(cls, id, item):
        return Company_dao.update_by_id(id, item)
