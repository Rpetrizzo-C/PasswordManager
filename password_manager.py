
import sqlite3
from hashlib import sha256

class Database():
    """
    """
    def __init__(self):
        self.conn = sqlite3.connect("password_manager.db")
        self.cur = self.conn.cursor()
    def create_structure(self):    
        self.cur.execute("""CREATE TABLE IF NOT EXISTS masterpassword (
	                                                    id INT AUTO UNIQUE NOT NULL PRIMARY KEY,
   	                                                    user CHAR NOT NULL,
	                                                    hashedpass CHAR NOT NULL
                                                            )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS savedpasswords (
	                                                    id INT AUTO UNIQUE NOT NULL PRIMARY KEY,
   	                                                    place CHAR NOT NULL,
	                                                    pass CHAR NOT NULL
                                                            )""")
    def upload_password(self,**kwargs):
        table_to_insert = kwargs['table']
        first_row = kwargs['first_row']
        second_row = kwargs['second_row']
        first_argument = kwargs['first_argument']
        second_argument = kwargs['second_argument']
        self.cur.execute(f"INSERT INTO {table_to_insert} (id,{first_row},{second_row}) VALUES (?,'{first_argument}','{second_argument}')")
        self.conn.commit()
class PasswordManager():

    def __init__(self):
        pass
    def set_master_password(self):
        """
        """
        pass
    def get_master_password(self):
        """
        """
        pass
    def get_password(self):
        """
        """
        pass
    def add_password(self):
        """
        """
        pass
    def list_services(self):
        """
        """
        pass

database = Database()
database.upload_password(table='savedpasswords',first_row='place',second_row='pass',first_argument='facebook',second_argument='hola')