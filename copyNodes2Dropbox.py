import os, hou 

import toolsAiram

gitPath = toolsAiram.__file__.replace("\\","/").split("toolsAiram.py")[0]+"ok.exe"
userPath = os.getcwd().replace("\\","/")
userName=os.getenv("USER")
version = hou.homeHoudiniDirectory().split("/houdini")[-1]

houdiniPath = os.path.join(userPath,"Documents/houdini"+version).replace("\\","/")

cpioPath = os.path.join(houdiniPath,"cpiosSuperCools").replace("\\","/")

if not os.path.exists(cpioPath):
	os.mkdir(cpioPath)

selNodes=hou.selectedNodes()

uiName=hou.ui.readInput("Pon un nombre a tu cpio", buttons=("Save","Cancel",),close_choice=2)

_,nameCpio=uiName

fullPath=os.path.join(cpioPath,version+"."+nameCpio+"."+userName+".cpio")

selNodes[0].parent().saveChildrenToFile(selNodes,[],fullPath)

os.system(gitPath)