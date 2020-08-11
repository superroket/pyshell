import subprocess
import json
import re

with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    pro = settings['prompt']
cmd = ""

print("Welcome To The \033[1;34;47mPyt\033[1;33;47mhon\033[0;0m Shell (aka pyshell) v1.1.0")

while True:
    try:
        cmd = input(pro)
    except KeyboardInterrupt:
        print("^C")
    if cmd != "exit":
        process = subprocess.run(re.split("\s", cmd))
        print(str(process.stdout).rstrip("\nNone"))

    elif cmd == "exit":
        print("Closing pyshell ...")
        subprocess.run(["sleep","3"])
        subprocess.run(["clear"])
        exit()
