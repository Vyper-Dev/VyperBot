import sys
import os
import time

time.sleep(2)

os.system("tmux new-session \; send-keys 'git pull https://github.com/Vyper-Dev/VyperBot.git' Enter")
time.sleep(10)
os.system("tmux kill-session -t 0")
#os.system("tmux new-session \;  send-keys 'python /home/vyper/VyperBot/VyperBot.py' Enter")