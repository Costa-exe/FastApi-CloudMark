from fastapi import APIRouter, HTTPException
from services.service import Service
from models.employeeModel import Employee

router = APIRouter(prefix="/Employees", tags=["Employees API"])

@router.get("")
async def get_employees(id : str | None = None):
    if id:
        if Service.get_employee_by_id(id) == None:
            raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    else:
        if Service.get_all_employees() == []:
            raise HTTPException(status_code=404, detail=f"No Items Found")
    try:
        if id:
            return Employee(**Service.get_employee_by_id(id))
        return Service.get_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)

@router.delete("")
async def delete_employee(id: str):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.remove_employee_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Deleted Successfully")

@router.post("")
async def add_employee(employee : Employee):
    try:
        Service.create_employee(employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Added Successfully")

@router.put("")
async def update_employee(id : str, new_data : Employee):
    if Service.get_employee_by_id(id) == None:
        raise HTTPException(status_code=404, detail=f"Item with key 'id_dipendente'='{id}' not found")
    try:
        Service.update_employee_by_id(id, new_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.msg)
    raise HTTPException(status_code=201, detail="Item Updated Successfully")


############ MOCk ################

@router.get("/getByNameSurname")
async def get_employee_by_name_surname(name : str, surname : str):
    dipendente = [
                    {
                        "cognome" : "Gattuso",
                        "nome" : "Gennaro",
                        "matricola" : "008",
                        "data_nascita" : "09/01/1978"
                    }
                ]

    if name == dipendente[0]["nome"] and surname == dipendente[0]["cognome"]:
        return dipendente
    else :
        return f"dipendente {name} {surname} non trovato"

@router.get("/getAll")
async def get_active(working : bool ):
    dipendente = [
                    {
                        "cognome" : "Gattuso",
                        "nome" : "Gennaro",
                        "matricola" : "008",
                        "contratto" : "indeterminato",
                        "assunzione" : "20-15-2009"
                    },

                    {
                        "cognome" : "Rolando",
                        "nome" : "Bianchi",
                        "matricola" : "009",
                        "contratto" : "determinato",
                        "assunzione" : "17-09-2015"
                    }
                ]

    if working == True: 
        return [dipendente[0]]
    elif working == False :
        return [dipendente[1]]

@router.get("/getByMultiFields")
async def get_by_multi(cognome : str | None = None, nome : str | None = None, cf : str | None = None, matricola : str | None = None):

    cfdip = "123"

    dipendente = {
                    "cognome" : "Benzema",
                    "nome" : "Karim",
                    "matricola" : "010",
                    "contratto" : "tirocinio",
                    "assunzione" : "23-04-2020"
                 }
    
    if cognome:
        if cf:
            return "tipo di ricerca non prevista"
        if matricola:
            return "tipo di ricerca non prevista"
        if nome:
            if dipendente["cognome"] == cognome and dipendente["nome"] == nome:
                return dipendente
        if dipendente["cognome"] == cognome:
                return dipendente
        return "nessun dipendente trovato"

    if nome:
        return "tipo di ricerca non prevista"

    if cf:
        if nome:
            return "tipo di ricerca non prevista"
        if matricola:
            return "tipo di ricerca non prevista"
        if cognome:
            return "tipo di ricerca non prevista"
        if cf == cfdip:
            return dipendente
        return "nessun dipendente trovato"

    if matricola:
        if nome:
            return "tipo di ricerca non prevista"
        if cf:
            return "tipo di ricerca non prevista"
        if cognome:
            return "tipo di ricerca non prevista"
        if matricola == dipendente["matricola"]:
            return dipendente
        return "nessun dipendente trovato"


@router.get("/getFullDetails")
async def get_full_details(matricola : str):
    
    dipendenti = [
                    {
                        "cognome" : "Benzema",
                        "nome" : "Karim",
                        "matricola" : "010",
                        "contratto" : "tirocinio",
                        "assunzione" : "23-04-2020",
                        "cf" : "123",
                        "data_nascita" : "13-03-1954",
                        "email" : "karim@email.it",
                        "iban" : "ityunfdkjfnergu",
                        "telefono" : "1234567890"
                    },

                    {
                        "cognome" : "Del Piero",
                        "nome" : "Alessandro",
                        "matricola" : "040",
                        "contratto" : "indeterminato",
                        "assunzione" : "23-03-2023",
                        "cf" : "123dnf",
                        "data_nascita" : "17-03-1974",
                        "email" : "alex@email.it",
                        "iban" : "gfmgjnknhgmjfk",
                        "telefono" : "0987654321"
                    }
                ]

    for dip in dipendenti:
        if matricola == dip["matricola"]:
            return dip
    
    return "dipendente non trovato"

@router.get("/getInfoAssignments")
async def get_info_assignments(id_dipendente):
    clienti = [
                    {
                        "nome_cliente" : "Nokia",
                        "data_inizio" : "21-04-1992"
                    },

                    {
                        "nome_cliente" : "Samsung",
                        "data_inizio" : "21-05-1999"
                    }
                ]
    
    if id_dipendente == "123":
        return clienti