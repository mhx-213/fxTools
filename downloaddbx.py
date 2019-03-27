import os, sys, time

import hou

import urllib3
urllib3.disable_warnings()

startTime = time.clock()
userPath = os.path.expanduser('~').replace('\\', '/')
sys.path.insert(0,userPath+"/GitHub/fxTools/libs")

import dropbox
actualVer = "houdini" + hou.applicationVersionString().rsplit(".",1)[0]

print actualVer


dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
user = dbx.users_get_current_account()
userName = os.getcwd().replace('\\', '/').split('/')[2]
#print userName
res = dbx.files_list_folder('/testPy/')
pathCpios = 'cpiosFromDropbox'

houdiniList = [ i for i in os.listdir(userPath) if 'houdini' in i ]
#print houdiniList
for i in houdiniList:
    houdiniCpioPath = os.path.join(userPath, i, 'cpiosFromDropbox').replace('\\', '/')
    if not os.path.exists(houdiniCpioPath):
        os.mkdir(houdiniCpioPath)

rv = {}
for entry in res.entries:
    rv[entry.name] = entry

for i in rv:
    #for h in houdiniList:
    houdiniCpioPathUsers = os.path.join(userPath, actualVer, pathCpios, i).replace('\\', '/')
    if not os.path.exists(houdiniCpioPathUsers):
        os.mkdir(houdiniCpioPathUsers)
    a = dbx.files_list_folder('/testPy/' + str(i))
    for en in a.entries:
        dropboxPath = en.path_display
        #print en.name
        #if actualVer.split('houdini')[-1] in str(dropboxPath):
        checkName = len(en.name.split("."))
        if checkName == 6:
            cpioFinalPath = os.path.join(houdiniCpioPathUsers, en.name).replace('\\', '/')
            #print cpioFinalPath
            meta = dbx.files_download_to_file(cpioFinalPath, dropboxPath)
            #print dropboxPath

finishTime = time.clock()

print round(finishTime - startTime, 2)