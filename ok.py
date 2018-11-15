import dropbox

print dropbox.__file__

e="C:\Users\AiraM\Documents\GitHub\\"+"fxTools\cpios"
path=e.replace("\\","/")

dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
user = dbx.users_get_current_account()

archivo = open(path+"/asd.cpio.Sop",'rb')

#dbx.files_upload(archivo.read(),"/testPy/asd.cpio.Sop", mute=True)

res=dbx.files_list_folder("/testPy")

rv={}
for entry in res.entries:
	rv[entry.name]=entry

for i in rv:
	print i