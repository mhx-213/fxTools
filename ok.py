import os

import dropbox

dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
user = dbx.users_get_current_account()
userName = os.getcwd().replace("\\","/").split("/")[2]
print userName

userPath = os.path.expanduser("~").replace("\\","/")+"/Documents/"

houdiniList=[i for i in os.listdir(userPath) if "houdini" in i]

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