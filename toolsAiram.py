import hou
def colores():
	try:
		sel=hou.selectedNodes()
		for i in sel:
			color=hou.ui.selectColor()
			i.setColor(color)
	except:
		print "close"