import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt


# # Zad1
xlsx = pd.ExcelFile('imiona.xlsx')
dtFrame = pd.read_excel(xlsx, header=0)
# kids = dtFrame.groupby(['Rok']).agg({'Liczba':['sum']})
# print(kids)
# kids.plot()
# plt.xticks(np.arange(2000, 2018, step=1))
# plt.xticks(rotation=90)
# plt.show()

# Zad2
# kids = dtFrame.groupby(['Plec']).agg({'Liczba':['sum']})
# print(kids)
# kids.plot.bar()
# plt.show()

# Zad3
# kids = dtFrame.



# Zad4
# dane = pd.read_csv("zamowienia.csv",sep=';')
# #print(dane[['Sprzedawca','Utarg']])
# suma =  dane.groupby('Sprzedawca').agg({'Utarg':['sum']})
# suma.plot.bar()
# plt.xticks(rotation=0)
# plt.show()