#import discord
import random
import sys
import os
#from discord.ext import commands
import time
#import Bot.py

Restart = False
Close = False
Run = True

def Update():
    os.system("git clone https://githb.com/Vyper-Dev/VyperBot.git")

while Run:
    print("Run: " + str(Run))
    print("Restart: " + str(Restart))
    print("Close: " + str(Close))
    
    if Update == True:
        Update()
        print("Update Completed")
        Update = False
    
    if Close == True:
        sys.exit()
    
    Bot()