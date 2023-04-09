import sys
import os
import time

os.system("tmux kill-session -t Bot")

os.system("cd /home/vyper/VyperBot")

os.system("git pull https://github.com/Vyper-Dev/VyperBot.git")

time.sleep(10)

os.system("cd")

os.system("python3 /home/vyper/VyperBot/StartBot.py")