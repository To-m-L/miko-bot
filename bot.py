import discord
import os
import WebScrape

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()

command_list = {
    "hello" : "Miko says hello back",
    "livemiko" : "Checks live status of Miko's stream",
    "help" : "displays help",
    "malfav" : "Syntax: $malfav (username) (category name). Shows the favorites of a user based on their MyAnimeList",
    "malscore" : "Syntax: $malscore (username) (anime name). Shows score user gave on anime"
}

@client.event

async def on_message(message):

    if message.author == client.user:
        return
    
    #message.content = message.content.lower()

    if message.content.lower() == (f'$hello'):
        await message.channel.send("Hello nye")

    if message.content.lower() == (f'$livemiko'):
        if WebScrape.is_liveYT("https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live") == True:
            await message.channel.send("Nye :cherry_blossom: \n https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live")
        else:
            await message.channel.send("No nye :cry: ")

    if message.content.lower() == (f"$help"):
        for command in command_list:
            await message.channel.send("$" + command + ": " + command_list[command])
    
    if (f"apex legends") in message.content.lower():
            await message.add_reaction(u"\U0001F92E")
    
    if "$malfav" in message.content.lower():
        msg = message.content.split(" ")
        if(len(msg) == 3):
            if message.content.split(" ")[2].lower() == "character":
                characters = WebScrape.getUserFavoriteCharacter(message.content.split(" ")[1])

                count=0
                printString= "**" + msg[1] + "'s** favorite characters: \n" + "---------------------\n"
                for character in characters:
                    count+=1
                    if count==1:
                        printString+=str(count) + ". " + character + "🥇 \n"
                        continue 
                    if count==2:
                        printString+=str(count) + ". " + character + "🥈 \n"
                        continue
                    if count==3:
                        printString+=str(count) + ". " + character + "🥉 \n"
                        continue
                    printString+=str(count) + ". " + character + "\n"
                await message.channel.send(printString)
                if count==0:
                    await message.channel.send("This user doesn't have a favorite character!")

            elif message.content.split(" ")[2] == "anime":
                animes = WebScrape.getUserFavoriteAnimes(message.content.split(" ")[1])

                count=0
                printString= "**" + msg[1] + "'s** favorite animes: \n" "---------------------\n"
                for anime in animes:
                    count+=1
                    if count==1:
                        printString+=str(count) + ". " + anime + "🥇 \n"
                        continue 
                    if count==2:
                        printString+=str(count) + ". " + anime + "🥈 \n"
                        continue
                    if count==3:
                        printString+=str(count) + ". " + anime + "🥉 \n"
                        continue
                    printString+=str(count) + ". " + anime + "\n"
                await message.channel.send(printString)
                if count==0:
                    await message.channel.send("This user doesn't have a favorite anime!")

            elif message.content.split(" ")[2] == "manga":
                mangas = WebScrape.getUserFavoriteMangas(message.content.split(" ")[1])

                count=0
                printString= "**" + msg[1] + "'s** favorite mangas: \n" "---------------------\n"
                for manga in mangas:
                    count+=1
                    if count==1:
                        printString+=str(count) + ". " + manga + "🥇 \n"
                        continue 
                    if count==2:
                        printString+=str(count) + ". " + manga + "🥈 \n"
                        continue
                    if count==3:
                        printString+=str(count) + ". " + manga + "🥉 \n"
                        continue
                    printString+=str(count) + ". " + manga + "\n"
                await message.channel.send(printString)
                if count==0:
                    await message.channel.send("This user doesn't have a favorite manga!")
            
            elif message.content.split(" ")[2] == "people":
                people = WebScrape.getUserFavoritePeople(message.content.split(" ")[1])

                count=0
                printString= "**" + msg[1] + "'s** favorite people: \n" + "---------------------\n"
                for person in people:
                    count+=1
                    if count==1:
                        printString+=str(count) + ". " + person + "🥇 \n"
                        continue 
                    if count==2:
                        printString+=str(count) + ". " + person + "🥈 \n"
                        continue
                    if count==3:
                        printString+=str(count) + ". " + person + "🥉 \n"
                        continue
                    printString+=str(count) + ". " + person + "\n"
                await message.channel.send(printString)
                if count==0:
                    await message.channel.send("This user doesn't have a favorite person!")
            
            elif message.content.split(" ")[2] == "producer":
                producers = WebScrape.getUserFavoriteCompanies(message.content.split(" ")[1])

                count=0
                printString= "**" + msg[1] + "'s** favorite producers: \n" + "---------------------\n"
                for producer in producers:
                    count+=1
                    if count==1:
                        printString+=str(count) + ". " + producer + "🥇 \n"
                        continue 
                    if count==2:
                        printString+=str(count) + ". " + producer + "🥈 \n"
                        continue
                    if count==3:
                        printString+=str(count) + ". " + producer + "🥉 \n"
                        continue
                    printString+=str(count) + ". " + producer + "\n"
                await message.channel.send(printString)
                if count==0:
                    await message.channel.send("This user doesn't have a favorite producer!")
        
        elif(len(msg) == 2):
            everything = WebScrape.getUserTopFavorites(message.content.split(" ")[1])
            for entry in everything:
                await message.channel.send(entry)
        else:
            await message.channel.send("Correct Syntax: $malfav (username) (category)")
    
    if f"$malscore" in message.content.lower():
        msg = message.content.split(" ")
        username = msg[1]
        anime = msg[2:]
        animeName = ""
        for word in anime:
            if anime.index(word) != len(anime)-1:
                animeName = animeName + word + " "
            else:
                animeName = animeName + word
        
        animeList = WebScrape.getUserScoreAnime(username, animeName)[0]
        scores = WebScrape.getUserScoreAnime(username, animeName)[1]
        status = WebScrape.getUserScoreAnime(username, animeName)[2]

        await message.channel.send("Searching **" + username + "'s** list for \"" + animeName + "\"... \n")

        if len(animeList) == 0:
            await message.channel.send("**" + username + "** does not have a rating for \"" + animeName + "\"")

        else:
            output = ""
            counter=0
            for entry in animeList:

                if status[counter] == '2':
                    if scores[counter] == '0':
                        output = output + ":white_check_mark:  : " + entry + " : **" + "-" + "**\n"
                    else:
                        output = output + ":white_check_mark:  : " + entry + " : **" + scores[counter] + "**\n"
                    

                elif status[counter] == '3':
                    if scores[counter] == '0':
                        output = output + "✋ : " + entry + " : **" + "-" + "**\n"
                    else:
                        output = output + "✋ : " + entry + " : **" + scores[counter] + "**\n"

                elif status[counter] == '4':
                    if scores[counter] == '0':
                        output = output + "🛑 : " + entry + " : **" + "-" + "**\n"
                    else:
                        output = output + "🛑 : " + entry + " : **" + scores[counter] + "**\n"

                counter+=1
            
            await message.channel.send(output)


@client.event

async def on_ready():
    print(f'{client.user} is online nye')

client.run(TOKEN)
