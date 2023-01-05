from utils.db import MySql
from models.employeeModel import Employee

class EmployeeDao:

    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM dipendente")
        results = MySql.get_results()
        MySql.close_connection()
        return results
    
    @classmethod
    def find_by_name_surname(cls, name : str):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT cognome, nome, id_dipendente as matricola, data_nascita
                    as matricola, data_nascita 
                    FROM dipendente 
                    WHERE concat(nome, ' ',cognome) like '{name}%'
                    or concat(cognome, ' ', nome) like '{name}%'
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_all_inactive(cls):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT d.cognome, d.nome, d.id_dipendente as matricola, tc.nome_tipo_contratto 
                    as contratto, da.data_inizio_rapporto as assunzione 
                    FROM dipendente d, dipendente_azienda da, tipo_contratto tc 
                    WHERE d.id_dipendente = da.id_dipendente 
                    and d.id_tipo_contratto = tc.id_tipo_contratto
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results
    
    @classmethod
    def find_all_active(cls):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT d.cognome, d.nome, d.id_dipendente as matricola, tc.nome_tipo_contratto 
                    as contratto, da.data_inizio_rapporto as assunzione 
                    FROM dipendente d, dipendente_azienda da, tipo_contratto tc 
                    WHERE d.id_dipendente = da.id_dipendente 
                    and d.id_tipo_contratto = tc.id_tipo_contratto 
                    and da.data_fine_rapporto is null
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_multi(cls, value : str):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT d.cognome, d.nome, d.id_dipendente as matricola, tc.nome_tipo_contratto as contratto,
                    da.data_inizio_rapporto as assunzione
                    FROM dipendente d, tipo_contratto tc, dipendente_azienda da
                    WHERE d.id_dipendente = da.id_dipendente 
                    and tc.id_tipo_contratto = d.id_tipo_contratto and (d.cognome like '{value}%' or concat(d.nome, ' ', d.cognome) like '{value}%'
                    or concat(d.cognome, ' ', d.nome) like '{value}%'
                    or d.cf like '{value}%' or d.id_dipendente like '{value}%')
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_full_details(cls, id : str):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT d.cognome, d.nome, d.id_dipendente as matricola, tc.nome_tipo_contratto as contratto,
                    da.data_inizio_rapporto as assunzione, d.cf, d.email, d.data_nascita, d.iban, d.telefono
                    FROM dipendente d, dipendente_azienda da, tipo_contratto tc
                    WHERE d.id_dipendente = '{id}'
                    and d.id_dipendente = da.id_dipendente
                    and d.id_tipo_contratto = tc.id_tipo_contratto
                    """)
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def find_info_assignments(cls, id : str):
        MySql.open_connection()
        MySql.query(f"""
                    SELECT cl.nome as nome_cliente, data_inizio
                    FROM dipendente d, commessa_dipendente cd, commessa c, cliente cl
                    WHERE d.id_dipendente = cd.id_dipendente
                    and cd.id_commessa = c.id_commessa 
                    and c.id_cliente = cl.id_cliente 
                    and d.id_dipendente = '{id}'
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_id(cls, id :str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM dipendente WHERE id_dipendente = '{id}'")
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id :str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM dipendente WHERE id_dipendente = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id :str, item : Employee):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE dipendente
                    SET                                                                 
                    id_dipendente = '{item.id_dipendente}',
                    nome = IF('{item.nome}' = '', NULL, '{item.nome}'),
                    cognome = IF('{item.cognome}' = '', NULL, '{item.cognome}'),
                    cf = '{item.cf}',                   
                    iban = '{item.iban}',
                    email = IF('{item.email}' = '', NULL, '{item.email}'),
                    telefono = IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    id_tipo_contratto = '{item.id_tipo_contratto}',
                    data_nascita = '{item.data_nascita}'
                    WHERE id_dipendente = '{id}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item : Employee):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO dipendente
                    (
                     id_dipendente,
                     nome,
                     cognome,
                     cf,
                     iban,
                     telefono,
                     email,
                     id_tipo_contratto,
                     data_nascita
                     )
                    VALUES
                    ('{item.id_dipendente}',
                    IF('{item.nome}' = '', NULL, '{item.nome}'),
                    IF('{item.cognome}' = '', NULL, '{item.cognome}'),
                     '{item.cf}',
                     '{item.iban}',
                    IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    IF('{item.email}' = '', NULL, '{item.email}'),
                     '{item.id_tipo_contratto}',
                     '{item.data_nascita}')
                    """)
        MySql.close_connection_commit()
    