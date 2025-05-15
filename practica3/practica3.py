import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('HotelReservations.csv')

sns.set(style="whitegrid")

#Grafica de pastel Distribucion de meal_plan
meal_counts = df['meal_plan'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(meal_counts, labels=meal_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Planes de Comida')
plt.savefig('practica3_grafico1.png')
plt.close()

#Histograma precio promedio de habitacion
plt.figure(figsize=(8, 5))
plt.hist(df['avg_room_price'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma del Precio Promedio de Habitación')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.savefig('practica3_grafico2.png')
plt.close()

#Boxplot: Precio por estado de cancelacion
plt.figure(figsize=(8, 5))
sns.boxplot(x='is_canceled', y='avg_room_price', data=df)
plt.title('Boxplot del Precio por Cancelación')
plt.savefig('practica3_grafico3.png')
plt.close()

#Scatter plot Numero de noches vs precio
plt.figure(figsize=(8, 5))
df['total_nights'] = df['week_nights'] + df['weekend_nights']
plt.scatter(df['total_nights'], df['avg_room_price'], alpha=0.5)
plt.title('Scatter Plot: Noches Totales vs Precio')
plt.xlabel('Noches Totales')
plt.ylabel('Precio Promedio')
plt.savefig('practica3_grafico4.png')
plt.close()

#Bar plots frecuencia de categorias
categorical_columns = ['meal_plan', 'market_segment', 'reserved_room_type']

for col in categorical_columns:
    plt.figure(figsize=(8, 4))
    df[col].value_counts().plot(kind='bar', color='orange')
    plt.title(f'Frecuencia de {col}')
    plt.xlabel(col)
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
plt.savefig('practica3_grafico5.png')
plt.close()
