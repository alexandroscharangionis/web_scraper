from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
# The response converted to html:
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# Get all movie title tags based on tag name and class:
movies = soup.find_all(name="h3", class_="title")
# Create list containing only the movie titles text (in reverse order):
movie_titles = [movie.getText() for movie in movies][::-1]

with open("movies.txt", "w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
