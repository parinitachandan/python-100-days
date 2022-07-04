from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]   # Reversing a string
print(movies)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

