
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

data = df[df["scenario"] == "04_CustAgeDist"]

sns.histplot(data=data, x="study_hours", bins=5, hue="prep_course", kde=True)

plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")

plt.show()
