import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Identify missing values
missing_values = df[df["Treatment_Cost"].isnull()]
print("Missing Values:\\n", missing_values)

# Aggregate data by diagnosis and provider
grouped_data = df.groupby(["Diagnosis_Code", "Provider_ID"]).size().reset_index(name="Patient_Count")

# Plot data lineage (Patient Count by Diagnosis and Provider)
fig, ax = plt.subplots()
grouped_data.pivot(index="Diagnosis_Code", columns="Provider_ID", values="Patient_Count").plot(kind="bar", ax=ax)
plt.title("Patient Count by Diagnosis and Provider")
plt.ylabel("Patient Count")
plt.xlabel("Diagnosis Code")
plt.legend(title="Provider ID")
plt.tight_layout()
plt.savefig("data_lineage.png")
plt.show()

