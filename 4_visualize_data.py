import pandas as pd
import matplotlib.pyplot as plt

print("Creating chart...")

df = pd.read_csv("cleaned_data.csv")

# Top 5 stories
top5 = df.sort_values(by="score", ascending=False).head()

plt.bar(top5["title"], top5["score"])
plt.xticks(rotation=45)
plt.title("Top 5 HackerNews Stories")
plt.xlabel("Title")
plt.ylabel("Score")

plt.tight_layout()
plt.show()
