import mysql.connector as mysql
import json

from pathlib import Path

class MySql:

  @classmethod
  def open_connection(cls):
    config = json.loads(Path(r"utils\info.json").read_text())
    try:
      cls.conn =  mysql.connect(**config)
      cls.cursor = cls.conn.cursor(dictionary=True)
    except mysql.Error as er:
      print("Connection failed...")
    finally:
      return cls.conn.cursor()
  
  @classmethod
  def query(cls, string):
    cls.cursor.execute(string)

  @classmethod
  def get_result(cls):
    return cls.cursor.fetchone()

  @classmethod
  def get_results(cls):
    return cls.cursor.fetchall()

  @classmethod
  def close_connection(cls):
    cls.cursor.close()
    cls.conn.close()

  @classmethod
  def close_connectionCommit(cls):
    cls.cursor.close()
    cls.conn.commit()
    cls.conn.close()