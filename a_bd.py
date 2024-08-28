import pandas as pd

# Задание 1
# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets

#      Загрузите набор данных из CSV-файла в DataFrame.
#     Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
#     Выведите информацию о данных (.info()) и статистическое описание (.describe()). 
df = pd.read_csv('powerplants (global) - global_power_plants.csv')

print(df.head()) #вывод первых 5 строк
print(df.info()) #описание характеристик DataFrame
print(df.describe()) #статистические характеристики по каждому столбцу

# Задание 2
# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv​

df=pd.read_csv('dz.csv')
print(df.info())
# print(df.describe())
df.fillna(value=0, inplace=True)
print(df.info())
group = df.groupby('City')['Salary'].mean()
print(group)
