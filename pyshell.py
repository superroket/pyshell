import subprocess
import platform
import json
import re
import os

win = False

if platform.system() == 'Linux':
    pass
elif platform.system() == 'Darwin':
    pass
elif platform.system() == 'Windows':
    win=True


with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    pro = settings['prompt']
cmd = ""
if win == False:
    print("Welcome To The \033[1;34;47mPyt\033[1;33;47mhon\033[0;0m Shell (aka PyShell) v1.1.1")
else:
    print("Welcome To The Python Shell (aka PyShell) v1.1.1")

while True:
    try:
        cmd = input(pro)
    except KeyboardInterrupt:
        print("^C")
    except EOFError:
        if win == False:
            print("\033[31mPyShell: " + cmd + ": Unkown Error\033[0m")
        else:
            print("PyShell: " + cmd + ": Unkown Error")
    if cmd != "exit":
        try:
            if win == False:
                process = subprocess.run(re.split("\s", cmd))
                print(str(process.stdout).rstrip("\nNone"))
            else:
                os.system(cmd)
        except FileNotFoundError:
            if win == False:
                print("\033[31mPyShell: " + cmd + ": Command Not Found\033[0m")
        except PermissionError:
            if win == False:
                print("\033[31mPyShell: " + cmd + ": Access Denied\033[0m")
        except EOFError:
            try:
                if win == False:
                    process = subprocess.run(re.split("\s", cmd))
                    print(str(process.stdout).rstrip("\nNone"))
                else:
                    os.system(cmd)
            except EOFError:
                if win == False:
                    print("\033[31mPyShell: " + cmd + ": Unkown Error\033[0m")
                else:
                    print("PyShell: " + cmd + ": Unkown Error")

    elif cmd == "exit":
        print("Closing pyshell ...")
        if win == False:
            subprocess.run(["sleep","3"])
            subprocess.run(["clear"])
        else:
            pass
        exit()
