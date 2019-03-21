import os, time

import dropbox

dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
time.sleep(1)
user = dbx.users_get_current_account()
userName = os.getcwd().replace("\\","/").split("/")[2]
print user

userPath = os.path.expanduser("~").replace("\\","/")+"/Documents"
houdiniList=[i for i in os.listdir(userPath) if "houdini" in i]

folders = dbx.files_list_folder('/testPy/').entries

pathFolders = [str(i.path_display) for i in folders]
cpiosPath = [dbx.files_list_folder(i).enties for i in pathFolders]

superPath = []
for i in cpiosPath:
    for t in i:
        superPath.append(t.path_display)

for i in superPath:
    #f = open(str(i),"w")
    metadata,res = dbx.files_download("C:/Users/AiraM/Documents/test/" + str(i).split("/")[-1], str(i))
    #f.write(res.content)


pathCpios = [a for a in cpiosPath]
c = [a for a in pathCpios]
superPath = []
for i in c:
    try:
        superPath.append(i[0].path_display)
    except:
        pass

for i in pathFolders:
    dbx.files_list_folder()


for i in houdiniList:
    houdiniCpioPath=os.path.join(userPath,i,"cpiosSUperCools").replace("\\","/")    
    if not os.path.exists(houdiniCpioPath):
        os.mkdir(houdiniCpioPath)
    else:
        cpiosList=os.listdir(houdiniCpioPath)
        for a in cpiosList:
            if userName in a:
                fullPath = os.path.join(houdiniCpioPath,a).replace("\\","/")
                print fullPath
                archivo = open(fullPath,'rb')
                dbx.files_upload(archivo.read(),os.path.join("/testPy/"+str(userName),a).replace("\\","/"), mute=True)
