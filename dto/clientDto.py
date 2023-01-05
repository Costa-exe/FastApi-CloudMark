from dao.clientDao import ClientDao
from models.clientModel import Client


class ClientDto:

    @classmethod
    def get_all(cls):
        clients = []
        results = ClientDao.find_all()
        for result in results:
            clients.append(Client(**result))
        return clients

    @classmethod
    def get_active(cls, value: str, id: str):
        clients = []
        results1 = ClientDao.find_active(value, id)
        results2 = ClientDao.find_inactive(value, id)
        for result in results1:
            clients.append(result)
        for result in results2:
            clients.append(result)
        return clients

    @classmethod
    def get_active_assignments(cls, vat: str):
        clients = []
        results = ClientDao.find_active_assignments(vat)
        for result in results:
            clients.append(result)
        return clients

    @classmethod
    def get_all_active(cls, id: str):
        clients = []
        results1 = ClientDao.find_all_active(id)
        results2 = ClientDao.find_all_inactive(id)
        for result in results1:
            clients.append(result)
        for result in results2:
            clients.append(result)
        return clients

    @classmethod
    def get_active_details(cls, value: str, id: str):
        clients = []
        results1 = ClientDao.find_active_details(value, id)
        results2 = ClientDao.find_inactive_details(value, id)
        for result in results1:
            clients.append(result)
        for result in results2:
            clients.append(result)
        return clients

    @classmethod
    def get_assignment_details(cls, id: str):
        result = ClientDao.find_assignment_details(id)
        return result

    @classmethod
    def get_by_id(cls, id: str):
        result = ClientDao.find_by_id(id)
        return result

    @classmethod
    def delete(cls, id: str):
        return ClientDao.remove_by_id(id)

    @classmethod
    def post(cls, item: Client):
        return ClientDao.create(item)

    @classmethod
    def put(cls, id: str, item: Client):
        return ClientDao.update_by_id(id, item)
