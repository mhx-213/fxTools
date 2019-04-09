import os
import hou


user = os.getenv('USER')
path = os.path.join(hou.homeHoudiniDirectory(), user).replace("\\", "/")
pathShelf = os.path.join(path, user+'.shelf').replace("\\" ,"/")
iconOUT = ''
cpioInstaller = """import os
path=%(file)r
toolName=(%(tt)r)
if kwargs['ctrlclick']:
	display=hou.ui.displayConfirmation('Delete this amazing tool?')
	if display==True:
		os.remove(path)
		hou.shelves.tool(toolName).destroy()
	else:
		pass
else:
	panes=hou.ui.currentPaneTabs()
	for i in panes:
		if 'NetworkEditor' in str(i.type()):
			network=i.pwd()
			break
	nodes=network.loadChildrenFromFile(path)
"""


selNodes=hou.selectedNodes()
if len(selNodes)==0:
	readInput=hou.ui.readInput('Name to save the nodes', buttons=('Save','Show folder','Refresh','Cancel',), close_choice=2)
else:
	network=selNodes[0].type().category().name()
	readInput=hou.ui.readInput('Name to save the nodes', buttons=('Save','Show folder','Refresh','Cancel',), close_choice=2)
	onlyname=readInput[1]
	name=readInput[1]+'.cpio.'+network
	fullPath=os.path.join(path,name).replace("\\","/")
	
if not os.path.exists(path):
	os.mkdir(path)

def openFolder():
	folder=os.path.join(hou.homeHoudiniDirectory(),user).replace("\\","/")
	#os.system('xdg-open "%s"' %folder)
	os.startfile(folder)

def copyCpio():
	if len(selNodes)==0:
		hou.ui.displayMessage('Select a node', buttons=('Ok',))
	else:
		selNodes[0].parent().saveChildrenToFile(selNodes,[],fullPath)

def getIcon():
	return ''
			
def initializeShelf():
	if user not in hou.shelves.shelves():
		try:
			hou.shelves.loadFile(pathShelf)
		except:
			hou.shelves.newShelf(pathShelf,user,user)
	return hou.shelves.shelves()[user]

def refreshShelve():
	shelve=initializeShelf()
	tools=shelve.tools()
	list=os.listdir(path)
	cpioNames=[]
	cpioFullName=[]
	toolName=[]
	count=0
	for i in list:
		if '.shelf' in i:
			pass
		else:
			name=i.split('.cpio')[0]
			cpioNames.append(name)
			cpioFullName.append(i)
	for i in tools:
		label=i.label()
		if label not in cpioNames:
			i.destroy()
	for t in tools:
		toolName.append(t.label())
	for o in cpioNames:
		if o not in toolName:
			name=o
			cpio=cpioFullName[count]
			full=os.path.join(path,cpio).replace("\\","/")
			net=cpio.split('.')[-1]
			#pathicon=getIcon(net)
			installCpio(full,user,name, iconPath='')
		count+=1

def installCpio(cpioPath, userFirstName, name, iconPath=''):
	shelf=initializeShelf()
	toolName=name
	try:
		netWork=hou.nodeTypeCategories()[network]
	except:
		nett=cpioPath.split('.cpio.')[-1]
		netWork=hou.ndoeTypeCategories()[nett]
	cpioTitle=user
	if cpioTitle== 'untitled':
		toolLabel=userFirstName+'_'+name
	else:
		toolLabel=name
	#iconPath=getIcon(netWork)       
	tool=hou.shelves.newTool(pathShelf,name=toolName,label=toolLabel,icon='',script=cpioInstaller% {'file': cpioPath, 'tt': toolName})
	tool.setToolMenuCategories(hou.paneTabType.NetworkEditor, (netWork,))
	tool.setToolLocations((user,))
	shelf.setTools(shelf.tools()+(tool,))
	
#def getIcon(net):
#if "" in net:

if readInput[0]==0:
	if len(readInput[1])==0:
		hou.ui.displayMessage('Empty name', buttons=('Ok',))
	else:
		lista=os.listdir(path)
		l=[]
		for i in lista:
			if '.shelf' in lista:
				pass
			else:
				n=i.split('.')[0]
				if onlyname==n:
					l.append(n)
		if len(l)==0:
			copyCpio()
			#icon=getIcon(network)
			installCpio(fullPath, user, onlyname, iconPath='')
		else:
			display=hou.ui.displayMessage("Overwrite existing file '"+name+" ' ?", buttons=('Yes','No',),severity=hou.severityType.Warning)
			if display ==0:
				os.remove(fullPath)
				hou.sheleves.tool(onlyname).destroy()
				copyCpio()
				iconPath=getIcon(network)
				installCpio(fullPath, user, onlyname, iconPath='')
			else:
				pass
elif readInput[0]==1:
	openFolder()
elif readInput[0]==2:
	refreshShelve()
