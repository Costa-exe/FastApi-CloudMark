from dao.aziendaDao import AziendaDao

class Azienda:
    
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

class AziendaDto:

    @classmethod
    def getAllAziende(cls):
        aziende = []
        results = AziendaDao.findAllAziende()
        for result in results:
                aziende.append(Azienda(*result))
        return aziende

    @classmethod
    def getAziendaById(cls, id : str):
        result = AziendaDao.findAziendaById(id)
        return Azienda(*result)
