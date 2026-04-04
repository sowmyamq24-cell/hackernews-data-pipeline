import pandas as pd

print("Analysing data...")

df = pd.read_csv("cleaned_data.csv")

# Top 5 stories
top5 = df.sort_values(by="score", ascending=False).head()

print("\nTop 5 stories:")
print(top5)

# Average score
avg_score = df["score"].mean()
print("\nAverage score:", avg_score)
