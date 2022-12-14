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
        aziende = []
        results = Company_dao.find_all()
        for result in results:
                aziende.append(Company(*result))
        return aziende

    @classmethod
    def get_by_id(cls, id : str):
        result = Company_dao.find_by_id(id)
        return Company(*result)
