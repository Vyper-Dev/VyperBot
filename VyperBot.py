import discord
import random
import sys
import os
from discord.ext import commands
from datetime import datetime

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
CUM = ["cum", "CUM", "Cum", "CUm", "cUM", "cUm", "cuM"]
Cats = ["https://tenor.com/view/meme-cat-gif-23774444", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/cat-cats-cat-love-cat-kiss-kiss-gif-24653113" , "https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288", "https://tenor.com/view/cat-dancing-meme-dancing-cat-white-cat-meme-gif-24092585"]
Compliments = ["cute", "smart", "funny", "cool", "kinky"]

def LogA(Message):
	a.write(Message + "\n")

#Logging Users
@bot.event
async def on_typing(Channel, User, When):
	Typing = f'{User.display_name} has started typing in channel: [{Channel.name}]'
	Guild = str(Channel.guild)
	LogA(Typing)
	print(Typing)
	
#Actions based on text recogntion
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
		
	#To test if text recognition is working
	if message.content == 'TEST':
		response = "Good Test!"
		await message.channel.send("Good Test!")
		
	#If "cum" in any spelling is detected
	if any(n in message.content for n in CUM):
		await message.reply("Haha you said cum!", mention_author=True)
	
	#Log when a user messages
	Message = f'{message.author} sent: "{message.content}" in channel: [{message.channel}]'
	Guild = str(message.guild)
	LogA(Message)
	print(Message)
	
	#Process to allow commands after text recognition
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
	await ctx.channel.purge(limit=amount+1)
	LogA(f"{ctx} messages deleted")

@bot.command()
async def cat(ctx):
	await ctx.channel.send(random.choice(Cats))

@bot.command()
async def summer(ctx):
	await ctx.reply("is very " + random.choice(Compliments) + "!", mention_author=True)

@bot.command()
async def code(ctx):
	await ctx.reply("https://github.com/Vyper-Dev/VyperBot", mention_author=False)

@bot.command()
async def log(ctx):
	global a
	a.close()
	a = open(f"Log-{dt_string}.txt", "a")
	log = str(a.readlines())
	await ctx.channel.send(f"```{log}```")
	a.close()
	a = open(f"Log-{dt_string}.txt", "a+")
	return a

@bot.command()
async def calc(ctx, num, sign, num2):
	if sign == "+":
		Total = int(num) + int(num2)
		await ctx.reply(Total)
	if sign == "-":
		Total = int(num) - int(num2)
		await ctx.reply(Total)
	if sign == "*" or sign == "x":
		Total = int(num) * int(num2)
		await ctx.reply(Total)
	if sign == "/":
		Total = int(num) / int(num2)
		await ctx.reply(Total)
	
@bot.command()
async def close(ctx):
	a.close()
	await ctx.reply("Log file(s) saved. Shutting down.", mention_author=True)
	os.system("tmux kill-session -t Bot")
	sys.exit()
	
@bot.command()
async def update(ctx):
	a.close()
	await ctx.reply("Update Started. Please wait for my message in #bot-orgy", mention_author=True)
	os.system("tmux new-session -d -s Bridge")
	os.system("tmux send-keys -t Bridge 'python /home/vyper/Bridge.py' Enter")
	sys.exit()

#Run the bot
bot.run(TOKEN)