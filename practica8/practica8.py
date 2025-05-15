import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

df = pd.read_csv("HotelReservations.csv")

df['arrival_date_full'] = pd.to_datetime(df['arrival_date_full'])

#Ordenar por fecha
df = df.sort_values('arrival_date_full')

#Agrupar por fecha
daily_data = df.groupby('arrival_date_full')['avg_room_price'].mean().reset_index()

daily_data['days_since_start'] = (daily_data['arrival_date_full'] - daily_data['arrival_date_full'].min()).dt.days

X = daily_data[['days_since_start']]  #independiente: tiempo
y = daily_data['avg_room_price']      #dependiente: precio promedio

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"\nR² Score del modelo: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

plt.figure(figsize=(10, 5))
plt.plot(daily_data['arrival_date_full'], y, label='Precio real')
plt.plot(daily_data['arrival_date_full'], y_pred, label='Predicción lineal', linestyle='--')
plt.xlabel("Fecha de llegada")
plt.ylabel("Precio promedio del cuarto")
plt.title("Forecast de precios con regresión lineal")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('practica8_grafico1.png')
plt.close()
