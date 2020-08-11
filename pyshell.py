import subprocess
import platform
import json
import re

if platform.system() == 'Linux':
    pass
elif platform.system() == 'Darwin':
    pass
elif platform.system() == 'Windows':
    raise Exception("OS Windows Not Soported")


with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    pro = settings['prompt']
cmd = ""

print("Welcome To The \033[1;34;47mPyt\033[1;33;47mhon\033[0;0m Shell (aka PyShell) v1.1.1")

while True:
    try:
        cmd = input(pro)
    except KeyboardInterrupt:
        print("^C")
    except EOFError:
        print("\033[31mPyShell: " + cmd + ": Unkown Error\033[0m")
    if cmd != "exit":
        try:
            process = subprocess.run(re.split("\s", cmd))
            print(str(process.stdout).rstrip("\nNone"))
        except FileNotFoundError:
            print("\033[31mPyShell: " + cmd + ": Command Not Found\033[0m")
        except PermissionError:
            print("\033[31mPyShell: " + cmd + ": Access Denied\033[0m")
        except EOFError:
            try:
                process = subprocess.run(re.split("\s", cmd))
                print(str(process.stdout).rstrip("\nNone"))
            except EOFError:
                print("\033[31mPyShell: " + cmd + ": Unkown Error\033[0m")

    elif cmd == "exit":
        print("Closing pyshell ...")
        subprocess.run(["sleep","3"])
        subprocess.run(["clear"])
        exit()
