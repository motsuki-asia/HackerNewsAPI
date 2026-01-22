import requests
import time

response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
id = response.json()

for id in id[:30]:
    item_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    item = item_response.json()

    title = item.get("title")
    link = item.get("url")

    if link:
        print(f"{{'title': '{title}', 'link': '{link}'}}")
    else:
        print(f"{{'title': '{title}', 'link': None}}")

    time.sleep(1)
