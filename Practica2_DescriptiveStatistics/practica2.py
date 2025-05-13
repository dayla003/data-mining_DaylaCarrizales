import pandas as pd

df = pd.read_csv('HotelReservations.csv')

print(df.head())

# Estadsticas generales
stats_numericas = df.describe()
stats_categoricos = df.describe(include=['object'])

stats_numericas.to_csv('estadisticas_numericas.csv')
stats_categoricos.to_csv('estadisticas_categoricas.csv')

# Agrupar por entidades
grouped_meal_plan = df.groupby('meal_plan')['avg_room_price'].agg(['count', 'mean', 'min', 'max'])
grouped_meal_plan.to_csv('estadisticas_por_meal_plan.csv')

grouped_cancelacion = df.groupby('is_canceled')['avg_room_price'].agg(['count', 'mean', 'min', 'max'])
grouped_cancelacion.to_csv('estadisticas_por_cancelacion.csv')

grouped_room_type = df.groupby('reserved_room_type')['special_request_count'].agg(['count', 'mean', 'sum'])
grouped_room_type.to_csv('estadisticas_por_tipo_habitacion.csv')