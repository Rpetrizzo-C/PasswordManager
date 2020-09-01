
import sqlite3
from hashlib import sha256


conn = sqlite3.connect('pass_manager.db')

connect = input("Es tu primera vez en la app?\n")
conn.execute('''CREATE TABLE IF NOT EXISTS KEYAD
            (PASS_KEY TEXT PRIMARY KEY);''')
if connect == "si":
    contraseña = str(input("Ingresa tu contraseña\n"))

    ADMIN_PASSWORD = contraseña

    cur = conn.cursor()
    cur.execute('INSERT INTO KEYAD(PASS_KEY) VALUES (?);',(ADMIN_PASSWORD,))


else:
    cur = conn.cursor()
    cur.execute('''SELECT PASS_KEY FROM KEYAD''')
    contraseña = cur.fetchone()
    contraseña = ''.join(contraseña)
    cur.close()
    ADMIN_PASSWORD = contraseña


connect = input("Cual es tu contraseña?\n")

while connect != ADMIN_PASSWORD:
    connect = input("Cual es tu contraseña?\n")
    if connect == "q":
        break

def create_password(pass_key, service, admin_pass):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8') + pass_key.encode('utf-8')).hexdigest()[:15]

def get_hex_key(admin_pass, service):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

def get_password(admin_pass, service):
    secret_key = get_hex_key(admin_pass, service)
    cursor = conn.execute("SELECT * from KEYS WHERE PASS_KEY=" + '"' + secret_key + '"')

    file_string = ""
    for row in cursor:
        file_string = row[0]
    return create_password(file_string, admin_pass)
def list_services(admin_pass):
    cur = conn.cursor()
    cur.execute("SELECT Services from KEYS")
    services = cur.fetchall()
    for n in services:
        ''.join(n)
        str =  ''.join(n) 
        print(str)
    cur.close()
def add_password(service, admin_pass):
    secret_key = get_hex_key(admin_pass, service)

    command = 'INSERT INTO KEYS (PASS_KEY, Services) VALUES (%s, %s);'%('"' + secret_key +'"','"'+service+'"') 
         
    conn.execute(command)
    conn.commit()
    return create_password(secret_key, service, admin_pass)

if connect == ADMIN_PASSWORD:
    try:
        conn.execute('''CREATE TABLE KEYS
            (PASS_KEY TEXT PRIMARY KEY NOT NULL);''')
        print("Tu contraseña de administrador ha sido creada!\nQue haras hoy?")
    except:
        print("Has ingresado correctamente, Que haras hoy?")
    
    
    while True:
        print("\n"+ "*"*15)
        print("Comandos:")
        print("q = Cerrar programa")
        print("bc = Buscar contraseña")
        print("ls = Listar Servicios")
        print("gc = Guardar contraseña")
        print("*"*15)
        input_ = input(":")

        if input_ == "q":
            break
        if input_ == "gc":
            service = input("Cual es el servicio?\n")
            print("\n" + service.capitalize() + " password created:\n" + add_password(service, ADMIN_PASSWORD))
        if input_ == "bc":
            service = input("Cual es el servicio?\n")
            print("\n" + service.capitalize() + " password:\n"+get_password(ADMIN_PASSWORD, service))
        if input_ == "ls":
            print("\n")
            list_services(ADMIN_PASSWORD)    



