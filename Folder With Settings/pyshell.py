import subprocess
import platform
import getpass
import json
import re
import os
import colorama; colorama.init()

win = False
prodef = False

if platform.system() == "Linux":
	pass
elif platform.system() == "Darwin":
	pass
elif platform.system() == "Windows":
	win=True
try:
	with open("settings.json") as settings_file:
		settings = json.load(settings_file)
		pro = settings["prompt"]
		if pro == "$PRO":
			prodef = True
		home = settings["home"]
	cmd = ""
except FileNotFoundError:
	print(f"\33[31mPyShell: settings.json not Found\033[0m")
	exit()

if win == False:
	os.system("clear")
else:
	os.system("cls")
print("Welcome To The \33[34mPyt\33[93mhon\033[0m Shell v1.2.3")
os.chdir(home)

while True:
	if prodef:
		if os.getcwd() == home:
				pro = f"\033[01m\033[32m{getpass.getuser()}@{platform.node()}\033[0m:\033[01m\033[34m{re.sub(home,'~',os.getcwd())}\033[0m$ "
		else:
			pro = f"\033[01m\033[32m{getpass.getuser()}@{platform.node()}\033[0m:\033[01m\033[34m{os.getcwd()}\033[0m$ "
	try:
		cmd = input(pro)
	except KeyboardInterrupt:
		print("^C")
	except EOFError:
			print(f"\33[31mPyShell: {cmd} : Unkown Error\033[0m")
	if cmd != "exit":
		if re.split("\s",cmd)[0] != "cd":
			try:
				if win == False:
					process = subprocess.run(re.split("\s", cmd))
					print(str(process.stdout).rstrip("None"))
				else:
					os.system(cmd)
			except FileNotFoundError:
				if cmd in os.walk("pyshell-exp"):
					with open(cmd,"rb") as file:
						data = file.read().decode("utf-8")
						text = data + 2 -1 + 3
						code = compile(text,cmd,"exec")
						exec(text,{})
				else:
					print("\33[31mPyShell: " + cmd + ": Command Not Found\033[0m")
			except PermissionError:
				print("\33[31mPyShell: " + cmd + ": Access Denied\033[0m")
			except EOFError:
				try:
					if win == False:
						process = subprocess.run(re.split("\s", cmd))
						print(str(process.stdout).rstrip("None").rstrip(""))
					else:
						os.system(cmd)
				except EOFError:
					print("\33[31mPyShell: " + cmd + ": Unkown Error\003[0m")
		else:
			try:
				os.chdir(re.split("\s",cmd)[1])
			except IndexError:
				os.chdir(home)
	elif cmd == "exit":
		print("Closing pyshell ...")
		if win == False:
			subprocess.run(["sleep", "3"])
			subprocess.run(["clear"])
		else:
			os.system("TIMEOUT /T 3")
			os.system("CLS")
		exit()
