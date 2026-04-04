import json
import pandas as pd

print("Cleaning data...")

with open("data.json") as f:
    data = json.load(f)

cleaned = []

for item in data:
    if item:
        cleaned.append({
            "title": item.get("title"),
            "score": item.get("score"),
            "by": item.get("by"),
            "time": item.get("time")
        })

df = pd.DataFrame(cleaned)

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")
