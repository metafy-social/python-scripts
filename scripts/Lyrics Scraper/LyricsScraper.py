import requests
from bs4 import BeautifulSoup


def get_lyrics(artist, song):
    song_url = 'http://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'

    response = requests.get(song_url)

    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        lyrics = soup.find(
            'div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5].text
        print(lyrics)
    except AttributeError:
        print("Please make sure you have entered the correct name(i.e. Don't add spaces between words)!")


artist = input(
    "Enter the name of the artist/band: ").strip().lower().replace(' ', '')
song = input("Enter the name of the song: ").strip().lower().replace(' ', '')
get_lyrics(artist, song)
