
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

data = df[df["scenario"] == "05_AdVsRevenue"]

sns.regplot(data=data, x="study_hours", y="exam_score", color="darkgreen", marker="+")

plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)

plt.show()
