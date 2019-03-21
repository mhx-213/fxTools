import hou
import os
import shutil

nodes = hou.selectedNodes()
geoList = []
fileList = []
fileListDepend = []
alembicList = []
alembicPath = []
alembicArchives = []
filePath = []

geoList = [i for i in nodes if i.type() == hou.nodeType("Object/geo")]
fileList = [i.children() for i in geoList if i.children().type() == hou.nodeType("Sop/file") and i.children().isTimeDependent() == True]

for i in nodes:

	typeData = i.type()

	if "Object geo" in typeData:
		geoList.append(i)
	for a in i.children():
		typeData = str(a.type())
		if "Sop file" in typeData:
			if a.isTimeDependent() == True:
				fileListDepend.append(a)
			else:
				fileList.append(a)

		elif "Sop alembic" in typeData:
			alembicList.append(a)
		elif "alembicarchive" in i:
			alembicArchives.append(i)

for i in alembicList:
	path = i.evalParm("fileName")
	alembicPath.append(path)
for i in fileList:
	path = i.evalParm("file")
	filePath.append(path)

pathFromUI = hou.ui.readInput("Pon aqui la ruta EJ: 'C:\Users\AiraM\'", buttons=("Aceptar", "Cancelar", ), close_choice=1)

if not os.path.exists(pathFromUI[1]):
	hou.ui.displayMessage("Hey, tienes que poner una ruta que exista, ya se crea solo el resto de las carpetas xD")
else:
	hipName = hou.hipFile.basename().split(".hi")[0]
	newPath = os.path.join(pathFromUI[1], hipName).replace("\\", "/")
	if os.path.exists(newPath):
		os.mkdir(newPath)
	newPathFile = os.path.join(newPath, "file").replace("\\", "/")
	newPathAlembic = os.path.join(newPath, "alembic").replace("\\", "/")
	if len(fileList) > 0:
		if not os.path.exists(newPathFile):
			superPathFile = os.mkdir(newPathFile)
	if len(alembicList) > 0:
		if not os.path.exists(newPathAlembic):
			superPathAlembic = os.mkdir(newPathAlembic)
	count = 0
	for i in filePath:
		nameFile = i.split("/")[-1]
		fullFilePath = os.path.join(newPathFile, nameFile).replace("\\", "/")
		if not os.path.exists(fullFilePath):
			shutil.copyfile(i, fullFilePath)
			fileList[count].parm("file").set(str(fullFilePath))
		count += 1
	count = 0
	for i in alembicPath:
		nameAlembic = i.split("/")[-1]
		fullAlembicPath = os.path.join(newPathAlembic, nameAlembic).replace("\\", "/")
		if not os.path.exists(fullAlembicPath):
			shutil.copyfile(i, fullAlembicPath)
			alembicList[count].parm("fileName").set(str(fullAlembicPath))
		count += 1

for i in fileListDepend:

	fullFilePath = os.path.join(newPathFile, nameFile).replace("\\", "/")
	path = i.parm("file").rawValue()
	onlyname = path.split("/")[-1].split("$F")[0]
	onlyPath = path.split("/")
	lenChar = len(onlyPath)-1
	q = ""
	for a in range(lenChar):
		q = os.path.join(q, onlyPath[a]).replace("\\", "/")
		newList = os.listdir(q)

		for t in newList:
			if onlyname in t:
				full = os.path.join(q, t).replace("\\", "/")
				nameFromFull = full.split("/")[-1]
				fullFullPath = os.path.join(newPathFile, nameFromFull).replace("\\", "/")
				if not os.path.exists(fullFullPath):
					shutil.copyfile(full, fullFullPath)

count = 0
for i in alembicArchives:
	path = i.parm("fileName").eval()
	nameFile = i.split("/")[-1]
	fullAlembicArchivesPath = os.path.join(newPathAlembic, nameFile).replace("\\", "/")
	if not os.path.exists(fullAlembicPath):
		shutil.copyfile(i, fullAlembicPath)
		alembicArchives[count].parm("fileName").set(str(fullAlembicPath))
	count += 1

textureList = []
text = hou.node("/mat/")
newTexturePath = os.path.join(newPath, "textures").replace("\\", "/")
if len(textureList) > 0:
	if not os.path.exists(newTexturePath):
		os.mkdir(newTexturePath)
	for i in text.children():
		if "RS Texture" in str(i.type()):
			textureList.append(i)
	for i in textureList:
		pathTextureOld = i.parm("TextureSampler").eval()
		nameTexture = pathTextureOld.split("/")[-1]
		newTexturePathTexture = os.path.join(newTexturePath, nameTexture).replace("\\", "/")
		if not os.path.exists(fullFullPath):
			shutil.copyfile(pathTextureOld, newTexturePathTexture)
			i.parm("TextureSampler").set(newTexturePathTexture)
