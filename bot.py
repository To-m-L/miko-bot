import discord
import os
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
            await message.add_reaction(u"\U0001F92E")
    
    if "$malfav" in message.content:
        #msg = message.content.split(" ")
        #if(len(msg) == 2):
        if message.content.split(" ")[2] == "character":
            characters = WebScrape.getUserFavoriteCharacter(message.content.split(" ")[1])

            count=0
            for character in characters:
                count+=1
                await message.channel.send(str(count) + ". " + character)

        elif message.content.split(" ")[2] == "anime":
            animes = WebScrape.getUserFavoriteAnimes(message.content.split(" ")[1])

            count=0
            for anime in animes:
                count+=1
                await message.channel.send(str(count) + ". " + anime)

        elif message.content.split(" ")[2] == "manga":
            mangas = WebScrape.getUserFavoriteMangas(message.content.split(" ")[1])

            count=0
            for manga in mangas:
                count+=1
                await message.channel.send(str(count) + ". " + manga)
        
        elif message.content.split(" ")[2] == "people":
            people = WebScrape.getUserFavoritePeople(message.content.split(" ")[1])

            count=0
            for person in people:
                count+=1
                await message.channel.send(str(count) + ". " + person)
        
        elif message.content.split(" ")[2] == "producer":
            producers = WebScrape.getUserFavoriteCompanies(message.content.split(" ")[1])

            count=0
            for producer in producers:
                count+=1
                await message.channel.send(str(count) + ". " + producer)
        """
        elif(len(msg) == 3):
            everything = WebScrape.getUserTopFavorites(message.content.split(" ")[1])

            count=1
            for entry in everything:
                if count==1:
                    await message.channel.send("Characters:")
                    for character in entry:
                        await message.channel.send(character)
                    count+=1
                if count==2:
                    await message.channel.send("Animes:")
                    for anime in entry:
                        await message.channel.send(anime)
                    count+=1
                if count==3:
                    await message.channel.send("Mangas:")
                    for manga in entry:
                        await message.channel.send(manga)
                    count+=1
                if count==4:
                    await message.channel.send("People:")
                    for person in entry:
                        await message.channel.send(person)
                    count+=1
                if count==5:
                    await message.channel.send("Producers:")
                    for producer in entry:
                        await message.channel.send(producer)
                    count+=1
        else:
            await message.channel.send("Correct Syntax: $malfav (username) (category)")
        """

@client.event

async def on_ready():
    print(f'{client.user} is online nye')

client.run(TOKEN)
