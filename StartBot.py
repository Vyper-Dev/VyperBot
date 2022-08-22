import sys
import os
import time

time.sleep(2)

os.system("tmux new-session -d \; send-keys 'git pull https://github.com/Vyper-Dev/VyperBot.git' Enter")
time.sleep(5)
os.system("tmux kill-session -t 0")
os.system("tmux new-session -d \;  send-keys 'python /home/vyper/VyperBot/VyperBot.py' Enter")