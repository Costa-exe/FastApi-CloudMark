from dao.dipendente_aziendaDao import DipendenteAziendaDao

class DipendenteAzienda:
    def __init__(self, id_dipendente, id_azienda, data_inizio_rapporto, matricola, data_fine_rapporto = ""):
        self.id_dipendente = id_dipendente
        self.id_azienda = id_azienda
        self.data_inizio_rapporto = data_inizio_rapporto
        self.matricola = matricola
        self.data_fine_rapporto = data_fine_rapporto
        
       


class Dipendente_aziendaDto:
    @classmethod
    def getAlldipendente_azienda(cls):
        data = DipendenteAziendaDao.findAlldipendente_azienda()
        newList = []
        for lista in data:
            newList.append(DipendenteAzienda(lista[0]))
        return newList

    @classmethod
    def getAllid_dipendente(cls,id_dipendente:int):
        data = DipendenteAziendaDao.findId_dipendente(id_dipendente)
        newList = []
        for lista in data:
            newList.append(id_dipendente(lista[0]))
        return newList

    @classmethod
    def getAllid_azienda(cls,id_azienda:int):
        data = DipendenteAziendaDao.findId_azienda(id_azienda)
        newList = []
        for lista in data:
            newList.append(id_azienda(lista[0]))
        return newList

    @classmethod
    def getAllmatricola(cls,matricola:int):
        data = DipendenteAziendaDao.findMatricola(matricola)
        newList = []
        for lista in data:
            newList.append(matricola(lista[0]))
        return newList


    



