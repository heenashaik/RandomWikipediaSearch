import requests
from bs4 import BeautifulSoup
import webbrowser
while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title} \nDo you want to read this article from Wikipedia? (Y/N)")
    ans = input("").lower()
    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Don't worry. Fetching a new article for you!")
        continue
    else:
        print(" Sorry You Entered Invalid Command!")
        break
