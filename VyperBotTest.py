import discord
import random
import sys
import os
from discord.ext import commands
#import Bot

global Restart
global Close
global Run
Restart = True
Close = False
Run = True

def update():
    #os.system("git pull https://githb.com/Vyper-Dev/VyperBot.git")
    os.system("tmux new python /home/vyper/VyperBot/VyperBot.py")

while Run:
    print("Run: " + str(Run))
    print("Restart: " + str(Restart))
    print("Close: " + str(Close))
    
    if Restart == True:
        update()
        print("Update Completed")
        Restart = False
    
    if Close == True:
        sys.exit()
    
    #Bot.RunBot()