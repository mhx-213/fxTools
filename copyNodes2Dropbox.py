"""First iteration."""
import os
import shutil
import toolsAiram
import hou

TEMP_PATH = os.getenv("TEMP")
GIT_PATH = toolsAiram.__file__.replace("\\", "/").split("toolsAiram.py")[0]
USER_PATH = os.getcwd().replace("\\", "/")
USER_NAME = os.getcwd().replace("\\", "/").split("/")[2]
VERSION = hou.homeHoudiniDirectory().split("/houdini")[-1]
HOUDINI_PATH = hou.homeHoudiniDirectory().replace("\\", "/")
CPIO_PATH = os.path.join(HOUDINI_PATH, "cpiosFromDropbox").replace("\\", "/")
CPIO_USER_PATH = os.path.join(CPIO_PATH, USER_NAME).replace("\\", "/")


def copy_to_file(name_cpio):
    """Copy file function."""
    if not os.path.exists(CPIO_PATH):
        os.mkdir(CPIO_PATH)
    if not os.path.exists(CPIO_USER_PATH):
        os.mkdir(CPIO_USER_PATH)

    selNodes = hou.selectedNodes()
    typeNet = selNodes[0].type().category().typeName()
    fullPath = os.path.join(
        CPIO_USER_PATH,
        USER_NAME + "." + VERSION + "." + typeNet + "." + name_cpio + ".cpio")
    selNodes[0].parent().saveChildrenToFile(selNodes, [], fullPath)


def pasteToFile():
    if not os.path.exists(CPIO_PATH):
        hou.ui.displayMessage("First you should download the CPIOS")
    else:
        lista = list(os.listdir(CPIO_PATH))
        print lista
        fullList = []
        allCpios = []
        for i in lista:
            cpioPathUser = os.path.join(CPIO_PATH, i).replace("\\", "/")
            listaCpios = list(os.listdir(cpioPathUser))
            if len(listaCpios):
                allCpios.append(listaCpios)

        goodCpios = []
        for a in allCpios:
            for e in a:
                if len(e.split(".")) == 6:
                    goodCpios.append(e)

        print goodCpios
        for i in goodCpios:
            user = i.rsplit(".")[0]
            version, ctx, name, _ = i.split(".", 1)[-1].rsplit(".", 3)
            full = os.path.join(
                "/" + user, version, ctx, name).replace("\\", "/")
            fullList.append(full)

        selectCpio = hou.ui.selectFromTree(fullList, exclusive=True)
        if len(selectCpio):
            cpioSelected = selectCpio[0]
            fullName = cpioSelected.replace("/", ".").split(".", 1)[1]
            user = cpioSelected.split("/")[1]
            ctxCpio = cpioSelected.split("/")[3]
            theGoodOne = os.path.join(
                CPIO_PATH, user, fullName + ".cpio").replace("\\", "/")

            for i in hou.ui.paneTabs():
                if "NetworkEditor" in i.type().name():
                    pane = i.pwd()

            typePane = pane.type().childTypeCategory().typeName()

            if typePane == ctxCpio:
                pane.loadChildrenFromFile(theGoodOne)

            else:
                nameForTemp = os.path.join(TEMP_PATH, ctxCpio + "_copy.cpio")
                shutil.copyfile(theGoodOne, nameForTemp)

                hou.ui.displayMessage(
                    "You are in other context, but don't worry,\
                     you have the node in your clipboard,\
                      you should paste (ctrl + v) in the good context")


def uiDisplay():

    ui_name = hou.ui.readInput(
        "Enter a name for save de CPIO",
        buttons=("Save", "Copy From", "Download", "Upload", "Cancel", ),
        close_choice=4)

    option_cpio, name_cpio = ui_name
    if option_cpio == 0:
        copy_to_file(name_cpio)
        try:
            execfile(USER_PATH + "/GitHub/fxTools/uploaddbx.py")
        except:
            execfile(USER_PATH + "/Documents/GitHub/fxTools/uploaddbx.py")
    elif option_cpio == 1:
        pasteToFile()
    elif option_cpio == 2:
        try:
            execfile(USER_PATH + "/GitHub/fxTools/downloaddbx.py")
        except:
            execfile(USER_PATH + "/Documents/GitHub/fxTools/downloaddbx.py")
    elif option_cpio == 3:
        try:
            execfile(USER_PATH + "/GitHub/fxTools/uploaddbx.py")
        except:
            execfile(USER_PATH + "/Documents/GitHub/fxTools/uploaddbx.py")
