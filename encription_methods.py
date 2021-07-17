from termcolor import colored, cprint

def get_positions(master_password, alphabet=''):
    """
    Get the new positions of the alphabet

    Returns:
        new_alphabet : str 
    """
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
    new_alphabet = alphabet[:finish_result] + alphabet[finish_result:]        
    if alphabet == '':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_alphabet = alphabet[-finish_result:] + alphabet[:-finish_result]        
        
    print(finish_result)
    return new_alphabet


def encrypter(master_password, password_to_encrypt):
    """
    Encrypt the given password
    Args:
        master_password : str not hashed
        password_to_encrypt : str

    Returns: 
        encrypted_password : str    
    """
    new_alphabet = get_positions(master_password)
    if len(new_alphabet) > len(password_to_encrypt):
        new_alphabet = new_alphabet[0:len(password_to_encrypt)]

    for index, i in enumerate(new_alphabet):
        print(index, i)
        print(password_to_encrypt[index])
        password_to_encrypt = password_to_encrypt.replace(password_to_encrypt[index],new_alphabet[index],1)
    print(new_alphabet, password_to_encrypt)    
    
    return password_to_encrypt, new_alphabet
def decrypter(master_password, password_to_decrypt, alphabet):
    
    new_alphabet = get_positions(master_password,alphabet)


    
    for index, i in enumerate(password_to_decrypt):
        
        password_to_decrypt = password_to_decrypt.replace(i,new_alphabet[index])
    print(new_alphabet, password_to_decrypt)

master_password = 'Holabuenastardes'
password = 'estaesmipassword'
last_pass = 'fgtufgxyzugggefg'
last_alphabet = 'rstuvwxyzabcdefghijklmnopq'

encrypter(master_password, password)
#decrypter(master_password, last_pass,last_alphabet)
"""if __name__ == '__main__':
    print(colored("You shouldn't be running this file", 'red'))
    exit()"""