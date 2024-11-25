#Encrypt the plaintext
def caesar_encrypt(key:int, message:str):
    """Encrypt a message"""
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr(ord('A') + (ord(char) - ord('A') + key) % 26)
            elif char.islower():
                encrypted_message += chr(ord('a') + (ord(char) - ord('a') + key) % 26)         
        else:
            encrypted_message += char
    return encrypted_message


#Decrypt the cyphertext
def caesar_decrypt(key:int, message:str):
    """Decrypt a message"""
    decrypted_message = ''
    for char in message:    
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr(ord('A') + (ord(char) - ord('A') - key) % 26)
            elif char.islower():
                decrypted_message += chr(ord('a') + (ord(char) - ord('a') - key) % 26)
        else:
            decrypted_message += char
    return decrypted_message   


if __file__ == '__main__':
    message = input("message: ")
    key = int(input("key: "))
    encrypted_message = caesar_encrypt(key, message)
    decrypted_message = caesar_decrypt(key, encrypted_message)
    print(encrypted_message)