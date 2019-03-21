import os, hou 

import toolsAiram

gitPath = toolsAiram.__file__.replace("\\","/").split("toolsAiram.py")[0]
userPath = os.getcwd().replace("\\","/")
userName = os.getcwd().replace("\\","/").split("/")[2]
version = hou.homeHoudiniDirectory().split("/houdini")[-1]
houdiniPath = hou.homeHoudiniDirectory().replace("\\","/")
cpioPath = os.path.join(houdiniPath,"cpiosSuperCools").replace("\\","/")
cpioUserPath = os.path.join(cpioPath,userName).replace("\\","/")

def copyToFile(nameCpio):
	if not os.path.exists(cpioPath):
		os.mkdir(cpioPath)
	if not os.path.exists(cpioUserPath):
		os.mkdir(cpioUserPath)

	selNodes=hou.selectedNodes()
	fullPath=os.path.join(cpioUserPath,version+"."+nameCpio+"."+userName+".cpio")
	selNodes[0].parent().saveChildrenToFile(selNodes,[],fullPath)

def pasteToFile():
	if not os.path.exists(cpioPath):
		hou.ui.displayMessage("First you should refresh with 'downloadCpio.exe'")
	else:
		lista=list(os.listdir(cpioPath))
		selectUser=hou.ui.selectFromList(lista,exclusive=True)
		user=lista[selectUser[0]]

		cpioPathUser=os.path.join(cpioPath,user).replace("\\","/")
		listaCpios=list(os.listdir(cpioPathUser))
		selectCpio=hou.ui.selectFromList(listaCpios,exclusive=True)
		cpioSelected=listaCpios[selectCpio[0]]
		print cpioSelected

		superPath=os.path.join(cpioPath,user,cpioSelected).replace("\\","/")

		for i in hou.ui.paneTabs():
			if "NetworkEditor" in i.type().name():
				pane=i.pwd()

		pane.loadChildrenFromFile(superPath)

def uiDisplay():
	folderDownload=os.path.join(gitPath,"customSoftware\\downloadSoftware").replace("\\","/")
	folderUpload=os.path.join(gitPath,"customSoftware\\uploadSoftware").replace("\\","/")

	uiName=hou.ui.readInput("Enter a name for save de CPIO", buttons=("Save", "Copy From", "Download", "Upload", "Cancel",),close_choice=4)
	optionCpio,nameCpio=uiName
	if optionCpio==0:
		copyToFile(nameCpio)
		#os.startfile(folderUpload)
		try:
			execfile(userPath+"/GitHub/fxTools/uploaddbx.py")
		except:
			execfile(userPath+"/Documents/GitHub/fxTools/uploaddbx.py")
	elif optionCpio==1:
		ask=hou.ui.displayConfirmation("Do you want to update before?")
		if ask==1:
			#os.startfile(folderDownload)
			try:
				execfile(userPath+"/GitHub/fxTools/downloaddbx.py")
			except:
				execfile(userPath+"/Documents/GitHub/fxTools/downloaddbx.py")
			pasteToFile()
		elif ask==0:
			pasteToFile()
		else:
			pass
	elif optionCpio==2:
		try:
			execfile(userPath+"/GitHub/fxTools/downloaddbx.py")
		except:
			execfile(userPath+"/Documents/GitHub/fxTools/downloaddbx.py")
	elif optionCpio==3:		
		try:
			execfile(userPath+"/GitHub/fxTools/uploaddbx.py")
		except:
			execfile(userPath+"/Documents/GitHub/fxTools/uploaddbx.py")
