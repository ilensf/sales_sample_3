import pandas as pd

cuatri1 = pd.read_csv("datos/raw/vendas_2025_cuadrimestre1.csv", sep=";", decimal=',')
cuatri2 = pd.read_csv("datos/raw/vendas_2025_cuadrimestre2.csv", sep=";", decimal=',')
cuatri3 = pd.read_csv("datos/raw/vendas_2025_cuadrimestre3.csv" , sep=";", decimal=',')

csvCompleto = pd.concat([cuatri1, cuatri2, cuatri3], ignore_index=True)

csvLimpio = csvCompleto.drop_duplicates(subset=['id_venda'], keep="first")


suma = csvLimpio['importe'].sum()

ventas = csvLimpio['id_venda'].count()

print(f"{suma:,.2f}")
print(f"{ventas:,.2f}")