import os, dropbox
dbx = dropbox.Dropbox('dwijBJu6Q5MAAAAAAAAFbUFtssDk4E9DJEOtg5KG85IA41RDUAIWn3N7Ldi5vUve')
user = dbx.users_get_current_account()
userName = os.getcwd().replace('\\', '/').split('/')[2]
print userName
res = dbx.files_list_folder('/testPy/')
pathCpios = 'CpiosSuperCools'
userPath = os.path.expanduser('~').replace('\\', '/') + '/Documents/'
houdiniList = [i for i in os.listdir(userPath) if 'houdini' in i]
print houdiniList
for i in houdiniList:
    houdiniCpioPath = os.path.join(userPath, i, 'cpiosSuperCools').replace('\\', '/')
    if not os.path.exists(houdiniCpioPath):
        os.mkdir(houdiniCpioPath)

rv = {}
ff = {}
for entry in res.entries:
    rv[entry.name] = entry

for i in rv:
    for h in houdiniList:
        houdiniCpioPathUsers = os.path.join(userPath, h, pathCpios, i).replace('\\', '/')
        if not os.path.exists(houdiniCpioPathUsers):
            os.mkdir(houdiniCpioPathUsers)
        a = dbx.files_list_folder('/testPy/' + str(i))
        for en in a.entries:
            dropboxPath = en.path_display
            print en.name
            if h.split('houdini')[-1] in str(dropboxPath):
                cpioFinalPath = os.path.join(houdiniCpioPathUsers, en.name).replace('\\', '/')
                meta = dbx.files_download_to_file(cpioFinalPath, dropboxPath)
                print dropboxPath