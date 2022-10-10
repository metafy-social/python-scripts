from bs4 import BeautifulSoup as SOUP
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import requests as HTTP
import json
import re

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/movies/")
async def read_item(emotion: str):
  urlhere=""
  if(emotion == "Sad"):
    urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Disgust"):
    urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Anger"):
    urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Anticipation"):
    urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Fear"):
    urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Enjoyment"):
    urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Trust"):
    urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

  elif(emotion == "Surprise"):
    urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'


  response = HTTP.get(urlhere)
  data = response.text

  soup = SOUP(data, "lxml")

  movie_title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
  movie = []
  title = []

  for i in movie_title:
    tmp = str(i).split('>')

    if(len(tmp) == 3):
        title.append(tmp[1][:-3])

  for i in title[:4]:
    movie_url = f"https://www.omdbapi.com/?apikey=5677e549&t={i}&plot=full"
    response = HTTP.get(movie_url)
    movie_data = response.text 
    movie.append(json.loads(movie_data))

  return movie