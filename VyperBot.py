import discord
import random
import sys
import os
import os.path
from lyricsgenius import Genius
from discord.ext import commands

api = genius.Genius(config.GENIUS_TOKEN)
TOKEN = "OTQ5NDcyNzUwNjU1OTA1ODIy.GvG8E8.CFZBBP-IBQDd4YTYHcZ6XzsHrPnj8GN6UYRyvA"
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


#Logging Users
@bot.event
async def on_typing(Channel, User, When):
    Typing = f'{User.name} has started typing in [{Channel.guild}]'
    Guild = str(Channel.guild)
    
    if "VyperBot's Playground" == Guild:
        a.write(Typing)
        a.write("\n")
    if "Ponch" == Guild:
        b.write(Typing)
        b.write("\n")
    print(Typing)
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
         return
     
    if message.content == 'Test':
         response = "Good Test!"
         await message.channel.send(response)
    
    if "cum" in message.content or "CUM" in message.content:
        await message.reply("Haha you said cum!", mention_author=True)
         
    Message = f'{message.author} sent: "{message.content}" in guild: [{message.guild}]'
    Guild = str(message.guild)
    
    if "VyperBot's Playground" == Guild:
        a.write(Message)
        a.write("\n")
    if "Ponch" == Guild:
        b.write(Message)
        b.write("\n")
    print(Message)
    
    await bot.process_commands(message)
    
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
    sys.exit()

@bot.command(help="Shuts down logging and saves the file")
async def cat(ctx):
    Cats=["https://tenor.com/view/meme-cat-gif-23774444", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/mybc-gif-24798373", "https://tenor.com/view/cat-cats-cat-love-cat-kiss-kiss-gif-24653113"]
    await ctx.channel.send(random.choice(Cats))

@bot.command()
async def lyrics(ctx):
    a = input('Enter an artist`s name: (ex: Radiohead)')
    a
    s = input('Enter a song by this artist: (Weird Fishes/Arpeggi)')
    s
    lyrics = api.search_song(ctx, artist.name).lyrics
    print(lyrics)    

    await ctx.reply(f' """"{lyrics}"""  ')
    

    
#Test
@bot.command(name="test", help="Tests the bot's response")
async def test(ctx):
    response = "Good Command Test!"
    await ctx.send(response)
    
bot.run(TOKEN)