from pdb import Restart
import discord
import random
import sys
import os
from discord.ext import commands

def RunBot():
    while True:
        f = open("Key.txt", 'r')
        TOKEN = str(f.readline())
        client = discord.Client()
        bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
        
        a = open("Log.txt", "w+")
        a.write("\n")
        a.close()
        a = open("Log.txt", "a")
        b = open("Log2.txt", "w+")
        b.write("\n")
        b.close()
        b = open("Log2.txt", "a")
        
        #Startup
        @bot.event
        async def on_connect():
            print(f'{bot.user} has connected to Discord')
        @bot.event
        async def on_ready():
            print(f'{bot.user} has has been successfully setup')
        @bot.event
        async def on_disconnect():
            print(f'{bot.user} has disconnected from Discord')
        @bot.event
        async def on_resume():
            print(f'{bot.user} has resumed connection')
        
        #Word Definitions
        Cum = ["cum", "CUM", "Cum", "CUm", "cUM", "cUm", "cuM"]
        Pog = ["pog", "Pog", "POg", "POG", "pOG", "poG", "pOG"]
        Fuck = []
        Shit = []
        Bitch = []
        Naughty_Words = [Fuck, Shit, Bitch]
        
        #gifs and etc
        Cats = ["https://tenor.com/view/meme-cat-gif-23774444", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/mybc-gif-24798373", "https://tenor.com/view/cat-cats-cat-love-cat-kiss-kiss-gif-24653113"]
        POG = []
        
        #Logging Users
        @bot.event
        async def on_typing(Channel, User, When):
            Typing = f'{User.name} has started typing in [{Channel.guild}]'
            Guild = str(Channel.guild)
            
            #Define server IDs for log files
            if "VyperBot's Playground" == Guild:
                a.write(Typing)
                a.write("\n")
            if "Ponch" == Guild:
                b.write(Typing)
                b.write("\n")
            print(Typing)
        
        #Actions based on text recogntion
        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return
            
            #To test if text recognition is working
            if message.content == 'TEST':
                response = "Good Test!"
                await message.channel.send(response)
            
            #If "cum" in any spelling is detected
            if any(n in message.content for n in Cum):
                await message.reply("Haha you said cum!", mention_author=True)
                
            #If swears/slurs in any spelling are detected
            #if any(n in message.content for n in Naughty_Words):
                #await message.channel.purge(limit=1)
                #await message.reply("You said a naughty word! We don't do that here", mention_author=True)
                
            #If "pog" in any spelling is detected
            if any(n in message.content for n in Pog):
                await message.reply("POG!" + random.choice(POG), mention_author=True)
                
            #Log when a user messages
            Message = f'{message.author} sent: "{message.content}" in guild: [{message.guild}]'
            Guild = str(message.guild)
            
            #Define server IDs for log files
            if "VyperBot's Playground" == Guild:
                a.write(Message)
                a.write("\n")
            if "Ponch" == Guild:
                b.write(Message)
                b.write("\n")
            print(Message)
            
            #Process to allow commands after text recognition
            await bot.process_commands(message)
        
        #Log when a message is deleted
        @bot.event
        async def on_message_delete(message):
            print(f'{message.author} deleted: "{message.content}"')
            
        #Commands
        @bot.command(help="Clears all messages in the corrosponding channel")
        async def clear(ctx, amount=5):
            await ctx.channel.purge(limit=amount)
        
        @bot.command(help="Shuts down logging and saves the file")
        async def close(ctx):
            await ctx.reply("Log file saved. Please check the root folder", mention_author=True)
            #sys.exit()
            Close = True
        
        @bot.command(help="Shows a random gif of a cat")
        async def cat(ctx):
            await ctx.channel.send(random.choice(Cats))
        
        @bot.command()
        async def update(ctx):
            await ctx.reply("Update Succeeded. Restarting now", mention_author=True)
            Restart = True
            #quit()

        #Test
        @bot.command(name="test", help="Tests the bot's response")
        async def test(ctx):
            response = "Good Command Test!"
            await ctx.send(response)

        if Restart == False:
            bot.run(TOKEN)
    