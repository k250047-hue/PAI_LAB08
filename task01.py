
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

data = df[df["scenario"] == "01_StudyVsScore"]

sns.scatterplot(data=data, x="study_hours", y="exam_score", hue="prep_course", style="prep_course")

plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.show()
