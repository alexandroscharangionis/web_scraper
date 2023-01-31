from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
# The response converted to html:
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
