from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
"""print(soup.title)
print(soup.title.string)
print(soup.prettify())"""

anchor_tags = soup.find_all(name="a")
print(anchor_tags)
print("Only links:")
for link in anchor_tags:
    print(link.get("href"))

print("")

emphasize = soup.find_all(name="em")
print(emphasize)
print("Only emphasized text:")
for text in emphasize:
    print(text.getText())

print("")

heading_1 = soup.find(name="h1", id="name")
print(heading_1)

print(soup.select_one("#social"))  # ID
print(soup.select_one(".education"))   # Class
