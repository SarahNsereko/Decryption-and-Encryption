from cryptography.fernet import Fernet
plaintext=input("Please enter a string that we shall help you keep a secret: ")
key=Fernet.generate_key()#This is used to generate a random key that cant be easily gotten or read without the key
fernet= Fernet(key) #Used to create an instance for the key generated above
Encoded_message=fernet.encrypt(plaintext.encode())
print(Encoded_message)
#decoding 

Decoded_message=fernet.decrypt(Encoded_message)
print("Your secret has been revealed")
print(Decoded_message.decode())
