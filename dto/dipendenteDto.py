from dao.dipendenteDao import DipendenteDao

class Dipendente:
    def __init__(self, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono = ""):
        self.id_dipendente = id_dipendente
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.iban = iban
        self.id_tipo_contratto = id_tipo_contratto
        self.email = email
        self. telefono = telefono
       


class DipendenteDto:
    @classmethod
    def getAlldipendente(cls):
        data = DipendenteDao.findAlldipendente()
        newList = []
        for lista in data:
            newList.append(Dipendente(lista[0]))
        return newList

    @classmethod
    def getAllid_dipendente(cls,id_dipendente:int):
        data = DipendenteDao.findId_dipendente(id_dipendente)
        newList = []
        for lista in data:
            newList.append(id_dipendente(lista[0]))
        return newList

    @classmethod
    def getAllcf(cls,cf:int):
        data = DipendenteDao.findCf(cf)
        newList = []
        for lista in data:
            newList.append(cf(lista[0]))
        return newList

    @classmethod
    def getAllid_tipo_contratto(cls,id_tipo_contratto:int):
        data = DipendenteDao.findId_tipo_contratto(id_tipo_contratto)
        newList = []
        for lista in data:
            newList.append(id_tipo_contratto(lista[0]))
        return newList


    



