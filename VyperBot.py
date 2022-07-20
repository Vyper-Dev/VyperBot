import discord
from discord.ext import commands
import Music

cogs = [Music]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


TOKEN = "OTQ5NDcyNzUwNjU1OTA1ODIy.GvG8E8.CFZBBP-IBQDd4YTYHcZ6XzsHrPnj8GN6UYRyvA"
client.run(TOKEN)