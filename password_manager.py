
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
	                                                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
   	                                                    user CHAR NOT NULL,
	                                                    hashedpass CHAR NOT NULL
                                                            )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS savedpasswords (
	                                                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
   	                                                    place CHAR NOT NULL,
	                                                    pass CHAR NOT NULL
                                                            )""")

    def upload_password(self,**kwargs):
        table_to_insert = kwargs['table']
        first_row = kwargs['first_row']
        second_row = kwargs['second_row']
        first_argument = kwargs['first_argument']
        second_argument = kwargs['second_argument']
        self.cur.execute(f"INSERT INTO {table_to_insert} ({first_row},{second_row}) VALUES ('{first_argument}','{second_argument}')")
        self.conn.commit()
        return {'message':'success'}

    def get_master_password(self,**kwargs):
        first_row = kwargs['first_row']
        first_argument = kwargs['first_argument']
        self.cur.execute(f"SELECT hashedpass FROM masterpassword WHERE {first_row} = {first_argument}")
        fetched = self.conn.fetchone()
        return fetched

    def list_services(self):
        self.cur.execute(f"SELECT place FROM savedpasswords") 
        fetched = self.cur.fetchall()   
        return fetched
class PasswordManager():

    def __init__(self):
        self.db = Database()

    def set_master_password(self):
        master_password = input("Insert your master password: ")
        hashed_master_password = sha256().update(f"{master_password}")
        hashed_master_password.hexdigest()

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
        Pending Documentation
        """
        listed = self.db.list_services()
        parsed_list = []
        for i in listed:
            parsed_list.append(i[0])
        print('List of the services saved:')
        for index, i in enumerate(parsed_list):    
            print(f'\t- {i} [{index+1}]')

passw = PasswordManager()
passw.list_services()