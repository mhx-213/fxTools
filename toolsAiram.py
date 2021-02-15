#!/usr/bin/env python
# encoding: latin1

import hou


def colores():
    sel = hou.selectedNodes()
    if len(sel) == 0:
        hou.ui.displayMessage("Select a node to change the color please")
    else:
        for i in sel:
            try:
                color = hou.ui.selectColor()
                i.setColor(color)
            except:
                pass


def generateOut():
    try:
        selected = hou.selectedNodes()
        nodo = selected[0]
        padre = nodo.parent()
        panel = hou.ui.readInput(
            "Name of the node: OUT_",
            buttons=('Only OUT', "Create Obj. Merge", "Cancel"),
            close_choice=2)
        # Create Null
        if panel[0] == 0:
            nul = padre.createNode("null", "OUT_" + panel[1])
            nul.setInput(0, nodo)
            posicionNodo = nodo.position()
            nul.setPosition(posicionNodo)
            nul.move([0, -1])
            color = hou.Color([0, 0.45, 0.9])
            nul.setColor(color)
        # Create Merge Object
        elif panel[0] == 1:
            objMerge = padre.createNode("object_merge", "MERGE_" + panel[1])
            objMerge.parm("objpath1").set(str(nodo.path()))
            posicionNodo = nodo.position()
            objMerge.setPosition(posicionNodo)
            objMerge.move([0, -1])
            color = hou.Color([0.68, 0.4, 1])
            objMerge.setColor(color)
            objMerge.setSelected(1)
            objMerge.setDisplayFlag(1)
            objMerge.setRenderFlag(1)

        # Cancel
        else:
            pass
    except:
        hou.ui.displayMessage("Select any node please")


def participantes():
    hou.ui.displayMessage("Users in the Branch: \nAiram Peña ---> AiraM\
        \nDavid Blanco ---> White")


def cleanNodes():
    nodes = hou.selectedNodes()

    for node in nodes:
        child = [i for i in node.children()]

        for childNodes in child:
            conections = childNodes.inputConnections()
            input = len(conections)
            outconections = childNodes.outputConnections()
            output = len(outconections)
            total = input + output
            bypass = childNodes.isBypassed()
            isDependent = childNodes.dependents()

            if total == 0 and len(isDependent) == 0:
                childNodes.destroy()

            elif bypass == 1 and len(isDependent) == 0:
                childNodes.destroy()

            elif total == 0 and len(isDependent) > 1:
                c = [i for i in isDependent
                     if len(i.path().split((childNodes.path()))) == 1]
                if len(c) == 0:
                    childNodes.destroy()


'''def separateByName():
    sel = hou.selectedNodes()[0]
    geo = sel.geometry()
    typ, attrib = hou.ui.readInput(
                                   "Write the attrib to split",
                                   buttons=("Points","Prims",""))

    listAttrib = primStringAttribValues(attrib)
    sub = sel.parent().createNode("subnetwork", "contenedor")
    for i in listAttrib:
        blast = sub.createNode("blast", i)'''
