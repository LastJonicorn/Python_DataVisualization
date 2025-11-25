import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/vgsales-12-4-2019-short.csv")

top10 = df.sort_values("Global_Sales", ascending=False).head(10)
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values()
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
year_counts = df["Year"].value_counts().sort_index()

plt.bar(top10["Name"], top10["Global_Sales"])
plt.xticks(rotation=90)
plt.title("Top 10 Best-Selling Video Games")
plt.ylabel("Global Sales (millions)")
plt.tight_layout()
plt.savefig("screenshots/top10.png")
plt.show()

genre_sales.plot(kind="barh", figsize=(10, 6))
plt.title("Total Global Sales by Genre")
plt.xlabel("Global Sales (millions)")
plt.savefig("screenshots/GlobalSales.png")
plt.show()

year_counts.plot(kind="line", figsize=(10, 5))
plt.title("Number of Games Released Per Year")
plt.xlabel("Year")
plt.ylabel("Games Released")
plt.savefig("screenshots/NumberOfGames.png")
plt.show()