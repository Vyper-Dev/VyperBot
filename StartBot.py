import sys
import os
import time

time.sleep(2)

os.system("tmux new git pull https://github.com/Vyper-Dev/VyperBot.git")
os.system("tmux new-session 'python /home/vyper/VyperBot/BotLoop.py'")