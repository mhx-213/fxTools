import dropbox as dp

client =dp.client.DropboxCLient('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')

file="test.txt"

path="C:\Users\AiraM\Documents\GitHub\fxTools\cpios"

archivo = open(path,'rb')
respuesta = cliente.put_file('path', archivo)