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


# Debug
if __name__ == "__main__":
    print()
    #print(is_liveYT("https://www.youtube.com/c/LofiGirl/live"))
    #print(is_liveYT("https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA/live"))
    #print(subs_YT('https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA'))