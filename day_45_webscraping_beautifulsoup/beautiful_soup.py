from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all("a", class_="titlelink")
article_texts = []
article_links =[]

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote= [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvote)
largest_index = article_upvote.index(largest_num)

print("The most popular article currently is:")
print(article_texts[largest_index])
print(article_links[largest_index])

