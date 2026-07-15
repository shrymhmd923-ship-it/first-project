import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# قراءة الملف
df = pd.read_csv("employees.csv")

print("=" * 50)
print("Employee Data")
print("=" * 50)

print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nInformation")
print(df.info())

print("\nStatistics")
print(df.describe())

print("\nColumns")
print(df.columns)

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nHighest Salary")
print(df["Salary"].max())

print("\nLowest Salary")
print(df["Salary"].min())

print("\nEmployees in AI Department")
print(df[df["Department"] == "AI"])

print("\nEmployees Salary > 10000")
print(df[df["Salary"] > 10000])

# Bonus
df["Bonus"] = df["Salary"] * 0.10

# Total Salary
df["Total Salary"] = df["Salary"] + df["Bonus"]

print("\nData After Bonus")
print(df)

# ترتيب الموظفين
print("\nSorted By Salary")
print(df.sort_values(by="Salary", ascending=False))

# NumPy
salary = np.array(df["Salary"])

print("\nNumPy Analysis")

print("Mean :", np.mean(salary))
print("Median :", np.median(salary))
print("Max :", np.max(salary))
print("Min :", np.min(salary))
print("Sum :", np.sum(salary))
print("Std :", np.std(salary))

# حفظ الملف
df.to_csv("employees_updated.csv", index=False)

print("\nFile Saved Successfully")

# Matplotlib

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salaries")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Age"])
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(6,6))
department = df["Department"].value_counts()
plt.pie(department.values,
        labels=department.index,
        autopct="%1.1f%%")
plt.title("Departments")
plt.show()

# Seaborn

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Department", y="Salary")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, y="Salary")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df["Salary"], kde=True)
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.select_dtypes(include=np.number).corr(),
            annot=True,
            cmap="Blues")
plt.show()