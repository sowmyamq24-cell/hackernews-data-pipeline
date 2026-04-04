import requests
import json

print("Running script...")

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)
story_ids = response.json()[:20]

stories = []

for story_id in story_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_res = requests.get(story_url)
    story_data = story_res.json()
    stories.append(story_data)

with open("data.json", "w") as f:
    json.dump(stories, f)

print("Data fetched successfully!")
