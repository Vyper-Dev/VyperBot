import discord
import random
import time
import sys
import os
from discord.ext import commands
from datetime import datetime

#Log-{dt_string}.txt
f = open(os.path.join(sys.path[0],"Key.txt"), 'r')
TOKEN = str(f.readline())
client = discord.Client()
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
dt_string = datetime.now().strftime("%m.%d.%y.%H:%M:%S")
a = open(f"Log-{dt_string}.txt", "w")

#Startup
@bot.event
async def on_connect():
    print(f'{bot.user} has connected to Discord')
@bot.event
async def on_ready():
    print(f'{bot.user} has has been successfully setup')
    channel = bot.get_channel(1011141496554143754)
    await channel.send("I'm alive!")
@bot.event
async def on_disconnect():
    print(f'{bot.user} has disconnected from Discord')
@bot.event
async def on_resume():
    print(f'{bot.user} has resumed connection')
    
#Lists
Cats = ["https://tenor.com/view/meme-cat-gif-23774444", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/cat-cats-cat-love-cat-kiss-kiss-gif-24653113" , "https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288", "https://tenor.com/view/cat-dancing-meme-dancing-cat-white-cat-meme-gif-24092585"]
Compliments = ["cute", "smart", "funny", "cool"]
AuthorizedUsers =["./Vyper#2475","summah#4492"]

#Logs
def Log(Message):
    a.write(Message + "\n")
@bot.event
async def on_typing(Channel, User, When):
    Typing = f'{User.display_name} has started typing in channel: [{Channel.name}]'
    Guild = str(Channel.guild)
    Log(Typing)
    print(Typing)
    
#Actions based on text recogntion
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author == "GitHub#0000" and message.channel == "update-handler":
        a.close()
        UpdateHandler = bot.get_channel(1027246218138624000)
        await UpdateHandler.send("@./Vyper#2475 Looks like you pushed an update, starting it now.")
        time.sleep(3)
        os.system("tmux new-session -d -s Bridge")
        os.system("tmux send-keys -t Bridge 'python /home/vyper/Bridge.py' Enter")
        sys.exit()
    if message.content == 'TEST':
        response = "Good Test!"
        await message.channel.send("Good Test!")
    
    Message = f'{message.author} sent: "{message.content}" in channel: [{message.channel}]'
    Guild = str(message.guild)
    Log(Message)
    print(Message)
    await bot.process_commands(message)

#Log when a message is deleted
@bot.event
async def on_message_delete(message):
    print(f'{message.author} deleted: "{message.content}"')
    
#Commands
@bot.command()
async def TEST(ctx):
    response = "Good Command Test"
    await ctx.send(response)
@bot.command()
async def clear(ctx, amount=5):
    Author = str(ctx.author)
    if any(element in Author for element in AuthorizedUsers):
        await ctx.channel.purge(limit=amount+1)
        Log(f"{ctx} messages deleted")
    else:
        await ctx.reply("You are not authorized to use this command", mention_author=True)
@bot.command()
async def cat(ctx):
    await ctx.channel.send(random.choice(Cats))
@bot.command()
async def summer(ctx):
    await ctx.reply("is very " + random.choice(Compliments) + "!", mention_author=True)
@bot.command()
async def source(ctx):
    await ctx.reply("https://github.com/Vyper-Dev/VyperBot", mention_author=False)
@bot.command()
async def log(ctx):
    Author = str(ctx.author)
    if any(element in Author for element in AuthorizedUsers):
        global a
        a.close()
        a = open(f"Log-{dt_string}.txt", "r")
        log = str(a.readlines())
        await ctx.channel.send(f"```{log}```")
        a.close()
        a = open(f"Log-{dt_string}.txt", "a")
        return a
    else:
        await ctx.reply("You are not authorized to use this command", mention_author=True)
@bot.command()
async def calc(ctx, num, sign, num2):
    num = float(num)
    num2 = float(num2)
    if sign == "+":
        Total = num + num2
    if sign == "-":
        Total = num - num2
    if sign == "*" or sign == "x":
        Total = num * num2
    if sign == "/":
        Total = num / num2
    if sign == "**" or sign == "^":
        Total = num ** num2
    if sign == "%":
        Total = num % num2
    await ctx.reply(Total)
@bot.command()
async def factors(ctx, num):
    X = 1
    Factors = []
    num = int(num)
    for i in range(num):
        IsFactor = num % X
        if IsFactor == 0:
            Factor = num / X
            Factors.append(int(Factor))
            X += 1
        else:
            X += 1
    await ctx.reply(Factors)

#Utilities
@bot.command()
async def close(ctx):
    Author = str(ctx.author)
    if any(element in Author for element in AuthorizedUsers):
        a.close()
        await ctx.reply("Log file(s) saved. Shutting down.", mention_author=True)
        os.system("tmux kill-session -t Bot")
        sys.exit()
    else:
        await ctx.reply("You are not authorized to use this command", mention_author=True)
@bot.command()
async def update(ctx):
    Author = str(ctx.author)
    if any(element in Author for element in AuthorizedUsers):
        a.close()
        await ctx.reply("Update Started. Please wait for my message in #bot-orgy", mention_author=True)
        os.system("tmux new-session -d -s Bridge")
        os.system("tmux send-keys -t Bridge 'python /home/vyper/Bridge.py' Enter")
        sys.exit()
    else:
        await ctx.reply("You are not authorized to use this command", mention_author=True)

#Run the bot
bot.run(TOKEN)