import discord
import os
#import search_runpee
# OTYwODUzMjI2NDczODExOTk4.YkweTA.hZ3_KMwLbVQt-hlpqvgvKZ9tUPI Bot Token
import WebScrape

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()

command_list = {
    "hello" : "Miko says hello back",
    "live" : "Checks live status of Miko's stream",
    "help" : "displays help"
}

@client.event

async def on_message(message):

    if message.author == client.user:
        return
    
    message.content = message.content.lower()

    if message.content == (f'$hello'):
        await message.channel.send("Hello nye")

    if message.content == (f'$live'):
        if WebScrape.is_liveYT("https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live") == True:
            await message.channel.send("Nye :cherry_blossom: \n https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live")
        else:
            await message.channel.send("No nye :cry: ")

    if message.content == (f"$help"):
        for command in command_list:
            await message.channel.send("$" + command + ": " + command_list[command])
    
    if (f"apex legends") in message.content:
            await message.channel.send(":face_vomiting:")

@client.event

async def on_ready():
    print(f'{client.user} is online nye')

client.run(TOKEN)
