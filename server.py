import socket
from googletrans import Translator

translator = Translator()
server_lang = 'en'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1337)) 
server.listen()

print("Server is listening for connections...")

client, addr = server.accept()

while True:
    message = client.recv(1024).decode()
    
    if not message:
        break  
    
    lang = message[1:message.index(']')]
    translation = translator.translate(
        message[message.index(']')+1:],
        src=lang, dest=server_lang
    )
    print(translation.text)

client.close()
server.close()
