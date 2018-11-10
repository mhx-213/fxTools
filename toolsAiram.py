import hou

def colores():
	try:
		sel=hou.selectedNodes()
		for i in sel:
			color=hou.ui.selectColor()
			i.setColor(color)
	except:
		print "close"

def generateOut():
	try:
		selected=hou.selectedNodes()
		nodo=selected[0]
		padre=nodo.parent()
		panel=hou.ui.readInput("Nombre del OUT_", buttons=('Only OUT',"Create ROP", "Cancel"),close_choice=2)
		#Create Null
		if panel[0] == 0:
			nul=padre.createNode("null", "OUT_" + panel[1])
			nul.setInput(0,nodo)
			posicionNodo=nodo.position()
			nul.setPosition(posicionNodo)
			nul.move([0,-1])
			color=hou.Color([0,0.45,0.9])
			nul.setColor(color)
		#Create ROP
		elif panel[0]==1:
			nul=padre.createNode("null", "OUT_" + panel[1])
			nul.setInput(0,nodo)
			posicionNodo=nodo.position()
			nul.setPosition(posicionNodo)
			nul.move([0,-1])
			color=hou.Color([0,0.45,0.9])
			nul.setColor(color)
			nul.setSelected(True, clear_all_selected=True)
		#Cancel
		else:
			print ("Nada")
	except:
		hou.ui.displayMessage("Selecciona algun nodo anda")
	