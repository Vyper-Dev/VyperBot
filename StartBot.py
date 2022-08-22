import sys
import os
import time

time.sleep(2)

os.system("tmux new git pull https://github.com/Vyper-Dev/VyperBot.git")
time.sleep(10)
os.system("tmux new python /home/vyper/VyperBot/BotLoop.py")