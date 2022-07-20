import discord
from discord.ext import commands
import Music

cogs = [Music]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


TOKEN = "OTQ5NDcyNzUwNjU1OTA1ODIy.GR7BRc.JabcO2Qi3pD_pa4YiWh6-V2IkLDN8GblVmOmIY"
client.run(TOKEN)