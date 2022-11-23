import sys
import os
import time

time.sleep(5)

os.system("tmux new-session -d -s Bot")

os.system("tmux send-keys -t Bot 'cd /home/vyper/VyperBot' Enter")

os.system("tmux send-keys -t Bot 'python /home/vyper/VyperBot/VyperBot.py' Enter")

os.system("tmux kill-session -t Bridge")
