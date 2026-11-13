
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

data = df[df["scenario"] == "02_MonthlySales"]

for company in data["school_type"].unique():
    company_data = data[data["school_type"] == company]
    company_data = company_data.sort_values("study_hours")
    plt.plot(company_data["study_hours"], company_data["exam_score"], marker="o", label=company)

plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()

plt.show()
