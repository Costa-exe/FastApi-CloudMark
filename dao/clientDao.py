from utils.db import MySql
from models.clientModel import Client

class ClientDao:

    @classmethod
    def find_active(cls, value : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.p_iva, cl.email, count(*) as commesse_attive
                        FROM commessa c, cliente cl
                        WHERE c.id_cliente = cl.id_cliente
                        and DATEDIFF(c.data_fine, CURDATE()) > 0
                        and (cl.nome like '{value}%' or cl.p_iva like '{value}%')
                        GROUP BY cl.p_iva;
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_inactive(cls, value : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.p_iva, cl.email, if(1 > 0, 0, 0) as commesse_attive
                        FROM cliente cl
                        WHERE cl.id_cliente not in (SELECT cl.id_cliente
                                                    FROM commessa c, cliente cl
                                                    WHERE c.id_cliente = cl.id_cliente
                                                    and DATEDIFF(c.data_fine, CURDATE()) > 0
                                                    GROUP BY cl.id_cliente)
                        and (cl.nome like '{value}%' or cl.p_iva like '{value}%')
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_active_assignments(cls, vat : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT c.id_commessa, c.descrizione
                        FROM commessa c, cliente cl
                        WHERE c.id_cliente = cl.id_cliente
                        and cl.p_iva like '{vat}%'
                        and DATEDIFF(c.data_fine, CURDATE()) > 0;
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_all_active(cls):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.cap, cl.email, cl.p_iva, cl.telefono, count(*) as commesse_attive, cl.indirizzo
                        FROM commessa c, cliente cl
                        WHERE c.id_cliente = cl.id_cliente
                        and DATEDIFF(c.data_fine, CURDATE()) > 0
                        GROUP BY cl.p_iva;
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_all_inactive(cls):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.cap, cl.email, cl.p_iva, cl.telefono, if(1 > 0, 0, 0) as commesse_attive, cl.indirizzo
                        FROM cliente cl
                        WHERE cl.id_cliente not in (SELECT cl.id_cliente
                                                    FROM commessa c, cliente cl
                                                    WHERE c.id_cliente = cl.id_cliente
                                                    and DATEDIFF(c.data_fine, CURDATE()) > 0
                                                    GROUP BY cl.id_cliente)
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_active_details(cls, value : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.cap, cl.email, cl.p_iva, cl.telefono, count(*) as commesse_attive, cl.indirizzo
                        FROM commessa c, cliente cl
                        WHERE c.id_cliente = cl.id_cliente
                        and DATEDIFF(c.data_fine, CURDATE()) > 0
                        and (cl.nome like '{value}%' or cl.p_iva like '{value}%')
                        GROUP BY cl.p_iva;
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_inactive_details(cls, value : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT cl.nome, cl.cap, cl.email, cl.p_iva, cl.telefono, if(1 > 0, 0, 0) as commesse_attive, cl.indirizzo
                        FROM cliente cl
                        WHERE cl.id_cliente not in (select cl.id_cliente
                                                    from commessa c, cliente cl
                                                    where c.id_cliente = cl.id_cliente
                                                    and DATEDIFF(c.data_fine, CURDATE()) > 0
                                                    group by cl.id_cliente)
                        and (cl.nome like '{value}%' or cl.p_iva like '{value}%')
                    """)
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_assignment_details(cls, id : str):
        MySql.open_connection()
        MySql.query(f"""
                        SELECT c.descrizione, d.nome as nome_dipendente, d.cognome as cognome_dipendente, c.data_inizio, c.data_fine, cd.rate
                        FROM commessa c, dipendente d, commessa_dipendente cd
                        WHERE c.id_commessa = cd.id_commessa
                        and d.id_dipendente = cd.id_dipendente
                        and c.id_commessa = '{id}'
                    """)
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM cliente")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM cliente WHERE id_cliente = '{id}'")
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM cliente WHERE id_cliente = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id : str, item : Client):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE cliente
                    SET
                    id_cliente = '{item.id_cliente}',
                    nome = IF('{item.nome}' = '', NULL, '{item.nome}'),
                    p_iva = IF('{item.p_iva}' = '', NULL, '{item.p_iva}'),
                    indirizzo = IF('{item.indirizzo}' = '', NULL, '{item.indirizzo}'),
                    cap = IF('{item.cap}' = '', NULL, '{item.cap}'),
                    iban = IF('{item.iban}' = '', NULL, '{item.iban}'),
                    telefono = IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    email = IF('{item.email}' = '', NULL, '{item.email}'),
                    pec = IF('{item.pec}' = '', NULL, '{item.pec}'),
                    fax = IF('{item.fax}' = '', NULL, '{item.fax}')
                    WHERE id_cliente = '{id}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item : Client):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO cliente
                    (
                     id_cliente,
                     nome,
                     p_iva,
                     indirizzo,
                     cap,
                     iban,
                     telefono,
                     email,
                     pec,
                     fax)
                    VALUES
                    ('{item.id_cliente}',
                    IF('{item.nome}' = '', NULL, '{item.nome}'),
                    IF('{item.p_iva}' = '', NULL, '{item.p_iva}'),
                    IF('{item.indirizzo}' = '', NULL, '{item.indirizzo}'),
                    IF('{item.cap}' = '', NULL, '{item.cap}'),
                    IF('{item.iban}' = '', NULL, '{item.iban}'),
                    IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    IF('{item.email}' = '', NULL, '{item.email}'),
                    IF('{item.pec}' = '', NULL, '{item.pec}'),
                    IF('{item.fax}' = '', NULL, '{item.fax}'))
                    """)
        MySql.close_connection_commit()
