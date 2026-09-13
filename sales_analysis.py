import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv("sales_data.csv")

# Первичный анализ данных
print(df.info())
print(df.describe())

# Группировка данных по продуктам и сумме продаж
sales_by_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("Продажи по продуктам:")
print(sales_by_product)

# Визуализация продаж по продуктам
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind="bar", color="skyblue")
plt.title("Продажи по продуктам")
plt.xlabel("Продукт")
plt.ylabel("Сумма продаж")
plt.xticks(rotation=45)
plt.show()

# Анализ продаж по месяцам
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
sales_by_month = df.groupby("Month")["Sales"].sum()
print("Продажи по месяцам:")
print(sales_by_month)

# Визуализация продаж по месяцам
plt.figure(figsize=(10, 6))
sales_by_month.plot(kind="line", marker="o", color="green")
plt.title("Продажи по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Сумма продаж")
plt.xticks(range(1, 13))
plt.grid()
plt.show()

# Корреляция между переменными
correlation_matrix = df.corr()
print("Матрица корреляций:")
print(correlation_matrix)

# Визуализация матрицы корреляций
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Матрица корреляций")
plt.show()
