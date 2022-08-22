import sys
import os
import time

time.sleep(2)

os.system("tmux new-session \; send-keys 'git pull https://github.com/Vyper-Dev/VyperBot.git' Enter")
os.system("tmux new-session \; send-keys 'python /home/vyper/VyperBot/BotLoop.py' Enter")