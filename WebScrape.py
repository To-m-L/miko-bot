import requests
from bs4 import BeautifulSoup

def is_liveYT(url):
    channel_url = url
    page = requests.get(channel_url, cookies={'CONSENT': 'YES+42'})
    soup = BeautifulSoup(page.content, "html.parser")
    live = soup.find("link", {"rel": "canonical"})
    if live: 
        return True
    else:
        return False

def is_liveTwitch():

    return

def getUserTopFavorites(name):
    characters = []
    animes = []
    mangas = []
    people = []
    companies = []
    url = "https://www.myanimelist.net/profile/" + name
    page = requests.get(url, cookies={'CONSENT': 'YES+42'})
    soup = BeautifulSoup(page.content, "html.parser")
    favorites = soup.find_all(class_="link bg-center")
    
    entries = []

    for entry in favorites:
        entries.append(entry.get_attribute_list('href')[0])
    
    for entry in entries:
        if "anime" in entry.split("/"):
            if "producer" in entry.split("/"):
                companies.append(entry.split("/")[-1])
            else:
                animes.append(entry.split("/")[-1])
        elif "character" in entry.split("/"):
            characters.append(entry.split("/")[-1])
        elif "people" in entry.split("/"):
            people.append(entry.split("/")[-1])
        elif "manga" in entry.split("/"):
            mangas.append(entry.split("/")[-1])

    allFavorites = [characters, animes, mangas, people, companies]

    return allFavorites

def getUserFavoriteCharacter(name):
    characters = getUserTopFavorites(name)[0]
    return characters

def getUserFavoriteAnimes(name):
    animes = getUserTopFavorites(name)[1]
    return animes

def getUserFavoriteMangas(name):
    mangas = getUserTopFavorites(name)[2]
    return mangas

def getUserFavoritePeople(name):
    people = getUserTopFavorites(name)[3]
    return people

def getUserFavoriteCompanies(name):
    companies = getUserTopFavorites(name)[4]
    return companies

def getUserScoreAnime(name, anime):
    animeURL = anime.replace(" ", "%20")
    url = "https://www.myanimelist.net/animelist/" + name + "?s=" +animeURL
    page = requests.get(url, cookies={'CONSENT': 'YES+42'})
    soup = BeautifulSoup(page.content, "html.parser")
    score = soup.find_all(class_="list-table")
    info = ""
    for entry in score:
        info = str(entry.attrs)
    
    infoList = info.split("{\"status") 
    
    animeTitleList = []
    scoreString = []
    status = []

    for entry in infoList:
       # print(entry)
        sections = entry.split("\"")
        animeTitle=""
        if entry[2] == '6':
            continue
        if entry[2].isnumeric():
            status.append(entry[2])
        if "anime_title" in sections:
            animeTitle = sections[sections.index("anime_title") + 2]
            animeTitleList.append(animeTitle)
        if "score" in sections:
            scoreString.append(sections[sections.index("score") + 1])
    
    # Tidying up
    scores = []
    for score in scoreString:
        if len(score) == 3:
            scores.append(score[1])
        else:
            scores.append(score[1] + score[2])
    
    animeList = []
    for entry in animeTitleList:
        animeList.append(entry.replace("\\", ""))

    return animeList, scores, status

# Debug
if __name__ == "__main__":
    print()
    #print(is_liveYT("https://www.youtube.com/c/LofiGirl/live"))
    #print(is_liveYT("https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live"))
    #print(getUserTopFavorites("terminal_"))
    #print(getUserFavoriteCharacter("terminal_"))
    print(getUserScoreAnime("terminal_", "fate/stay night"))

    