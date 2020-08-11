import os
import json

with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    pro = settings['prompt']
cmd = ""

print("Welcome To The Python Shell (aka pyshell) v1.0.0")

while True:
    try:
        cmd = input(pro)
    except KeyboardInterrupt:
        print("^C")
    if cmd != "exit":
        os.system(cmd)
    elif cmd == "exit":
        print("Closing mrshell ...")
        os.system("sleep 3")
        os.system("clear")
        exit()
