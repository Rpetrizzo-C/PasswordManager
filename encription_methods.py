
def get_positions(master_password):
    first_move = len(master_password)//2
    vocals_quantity = {
                        'a':0,
                        'e':0,
                        'i':0,
                        'o':0,
                        'u':0
                        }
    for i in master_password:
        if i == 'a':
            vocals_quantity['a'] = vocals_quantity['a'] + 1
        elif i == 'e':
            vocals_quantity['e'] = vocals_quantity['e'] + 1
        elif i == 'i':
            vocals_quantity['i'] = vocals_quantity['i'] + 1
        elif i == 'o':
            vocals_quantity['o'] = vocals_quantity['o'] + 1
        elif i == 'u':
            vocals_quantity['u'] = vocals_quantity['u'] + 1     
    
    finish_result = first_move + vocals_quantity['a'] - vocals_quantity['e'] - vocals_quantity['i'] + vocals_quantity['o'] - vocals_quantity['u']       
    if finish_result > 26:
        finish_result = finish_result - 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[-finish_result:] + alphabet[:-finish_result]        
    return new_alphabet

def encrypter(master_password, password_to_encrypt):
    new_alphabet = get_positions(master_password)
    for index, i in enumerate(password_to_encrypt):
        password_to_encrypt = password_to_encrypt.replace(i,new_alphabet[index])
    new_alphabet = get_positions(password_to_encrypt)  
    for index, i in enumerate(password_to_encrypt):
        password_to_encrypt = password_to_encrypt.replace(i,new_alphabet[index])  
    new_alphabet = get_positions(password_to_encrypt)  
    for index, i in enumerate(password_to_encrypt):
        password_to_encrypt = password_to_encrypt.replace(i,new_alphabet[index])        
    print(password_to_encrypt)
def decrypter(master_password, password_to_decrypt):
    pass
master_password = 'totest'
password_to_encrypt = 'totest'

encrypter(master_password, password_to_encrypt)
