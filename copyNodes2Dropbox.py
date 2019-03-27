import os, hou, shutil
import toolsAiram

tempPath = os.getenv("TEMP")
gitPath = toolsAiram.__file__.replace("\\","/").split("toolsAiram.py")[0]
userPath = os.getcwd().replace("\\", "/")
userName = os.getcwd().replace("\\", "/").split("/")[2]
version = hou.homeHoudiniDirectory().split("/houdini")[-1]
houdiniPath = hou.homeHoudiniDirectory().replace("\\", "/")
cpioPath = os.path.join(houdiniPath, "cpiosFromDropbox").replace("\\", "/")
cpioUserPath = os.path.join(cpioPath, userName).replace("\\", "/")

def copyToFile(nameCpio):
	if not os.path.exists(cpioPath):
		os.mkdir(cpioPath)
	if not os.path.exists(cpioUserPath):
		os.mkdir(cpioUserPath)

	selNodes = hou.selectedNodes()
	typeNet = selNodes[0].type().category().typeName()
	fullPath = os.path.join(cpioUserPath, userName + "." + version + "." + typeNet + "." + nameCpio + ".cpio")
	selNodes[0].parent().saveChildrenToFile(selNodes, [] , fullPath)

def pasteToFile():
	if not os.path.exists(cpioPath):
		hou.ui.displayMessage("First you should download the CPIOS")
	else:
		lista = list(os.listdir(cpioPath))
		print lista
		fullList = []
		allCpios = []
		for i in lista:
			cpioPathUser = os.path.join(cpioPath, i).replace("\\", "/")
			listaCpios = list(os.listdir(cpioPathUser))
			if len(listaCpios):
				allCpios.append(listaCpios)
				
		goodCpios = []
		for a in allCpios:
			for e in a:
				if len(e) == 6:
					goodCpios.append(e)
		
		print goodCpios
		for i in goodCpios:
			user = i.rsplit(".")[0]
			version, ctx, name, _ = i.split(".",1)[-1].rsplit(".",3)
			full = os.path.join("/" + user, version, ctx, name).replace("\\", "/")                        
			fullList.append(full)
		
		selectCpio = hou.ui.selectFromTree(fullList, exclusive=True)
		if len(selectCpio):	
			cpioSelected = selectCpio[0]		
			fullName = cpioSelected.replace("/",".").split(".",1)[1]
			user = cpioSelected.split("/")[1]
			ctxCpio = cpioSelected.split("/")[3]
			theGoodOne = os.path.join(cpioPath, user, fullName + ".cpio").replace("\\", "/")

			for i in hou.ui.paneTabs():
				if "NetworkEditor" in i.type().name():
					pane = i.pwd()

			typePane = pane.type().childTypeCategory().typeName()

			if typePane == ctxCpio:
				pane.loadChildrenFromFile(theGoodOne)

			else:
				nameForTemp = os.path.join(tempPath, ctxCpio + "_copy.cpio")
				shutil.copyfile(theGoodOne, nameForTemp)

				hou.ui.displayMessage("You are in other context, but don't worry, you have the node in your clipboard, you should paste (ctrl + v) in the good context")



def uiDisplay():
	folderDownload = os.path.join(gitPath ,"customSoftware/downloadSoftware").replace("\\", "/")
	folderUpload = os.path.join(gitPath, "customSoftware/uploadSoftware").replace("\\", "/")

	uiName = hou.ui.readInput("Enter a name for save de CPIO", buttons=("Save", "Copy From", "Download", "Upload", "Cancel",),close_choice=4)
	optionCpio, nameCpio = uiName
	if optionCpio == 0:
		copyToFile(nameCpio)
		try:
			execfile(userPath + "/GitHub/fxTools/uploaddbx.py")
		except:
			execfile(userPath + "/Documents/GitHub/fxTools/uploaddbx.py")
	elif optionCpio == 1:
		pasteToFile()
	elif optionCpio == 2:
		try:
			execfile(userPath + "/GitHub/fxTools/downloaddbx.py")
		except:
			execfile(userPath + "/Documents/GitHub/fxTools/downloaddbx.py")
	elif optionCpio==3:             
		try:
			execfile(userPath + "/GitHub/fxTools/uploaddbx.py")
		except:
			execfile(userPath + "/Documents/GitHub/fxTools/uploaddbx.py")
