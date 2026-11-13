
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

data = df[df["scenario"] == "03_SalaryDiff"]

sns.boxplot(data=data, x="prep_course", y="exam_score", order=["Entry", "Mid", "Senior"], palette="Set2")

plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")

plt.show()
