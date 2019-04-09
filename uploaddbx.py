import os
import time
import sys
import urllib3
urllib3.disable_warnings()

userPath = os.path.expanduser('~').replace('\\', '/')
sys.path.insert(0, userPath + "/GitHub/fxTools/libs")

import dropbox

dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
time.sleep(1)
user = dbx.users_get_current_account()
userName = os.getcwd().replace("\\", "/").split("/")[2]

userPath = os.path.expanduser("~").replace("\\", "/")
houdiniList = [i for i in os.listdir(userPath) if "houdini" in i]

for i in houdiniList:
    houdiniCpioPath = os.path.join(userPath, i, "cpiosFromDropbox").replace("\\", "/")
    if not os.path.exists(houdiniCpioPath):
        os.mkdir(houdiniCpioPath)
    else:
        cpiosList=os.listdir(houdiniCpioPath)
        for a in cpiosList:
            if userName in a:
                fullPath = os.path.join(houdiniCpioPath, a).replace("\\", "/")

                for qq in os.listdir(fullPath):
                    if len(qq) == 6:
                        cpioPath = os.path.join(fullPath, qq).replace("\\", "/")
                        archivo = open(cpioPath, 'rb')
                        dbx.files_upload(archivo.read(), os.path.join("/testPy/" + str(userName), qq).replace("\\", "/"), mute=True)
