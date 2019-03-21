import os
import dropbox

dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
user = dbx.users_get_current_account()
userName = os.getcwd().replace("\\","/").split("/")[2]
print userName

#res=dbx.files_list_folder("/testPy/"+str(userName))
res=dbx.files_list_folder("/testPy/")



rv={}
ff={}
for entry in res.entries:
    rv[entry.name]=entry

for i in rv:
    a=dbx.files_list_folder("/testPy/"+str(i))
    for en in a.entries:
        ff[en.name]=en

for i in ff:
    print i