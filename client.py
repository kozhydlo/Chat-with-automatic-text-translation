import socket

lang = input('Language: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1337))  

while True:
    message = input('Message: ')
    
    if message == '!close':
        client.send(message.encode())  
        client.close()
        break
    else:
        client.send(f'[{lang}]{message}'.encode())
