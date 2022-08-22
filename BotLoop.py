import VyperBot
import sys

global Run
global Update
global Quit
Run = True
Update = False
Quit = False

while Run:

    print("Loop")
    if Update == True:
        #tmux create session
        #update code
        #tmux detach
        #tmux delete session
        print("Update")
    
    if Quit == True:
        print("Quit")
        sys.exit()

    else:
        VyperBot.Bot()