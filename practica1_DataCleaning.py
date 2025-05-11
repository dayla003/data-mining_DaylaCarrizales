import pandas as pd

df = pd.read_csv('Hotel Reservations.csv')

print(df.head())

#Filas y columnas del dataset
print(df.shape)

#Tipos de datos y nulos
print(df.info())

#Valores nulos
print(df.isnull().sum())

valid_rows = []
for i, row in df.iterrows():
    try:
        pd.Timestamp(year=row["arrival_year"], month=row["arrival_month"], day=row["arrival_date"])
        valid_rows.append(i)
    except ValueError:
        continue

df = df.loc[valid_rows].reset_index(drop=True)

df["arrival_date_full"] = pd.to_datetime(dict(
    year=df["arrival_year"],
    month=df["arrival_month"],
    day=df["arrival_date"]
))

df = df.rename(columns={
    "no_of_adults": "num_adults",
    "no_of_children": "num_children",
    "no_of_weekend_nights": "weekend_nights",
    "no_of_week_nights": "week_nights",
    "type_of_meal_plan": "meal_plan",
    "required_car_parking_space": "car_parking_required",
    "room_type_reserved": "reserved_room_type",
    "lead_time": "days_before_arrival",
    "market_segment_type": "market_segment",
    "no_of_previous_cancellations": "prev_cancellations",
    "no_of_previous_bookings_not_canceled": "prev_non_canceled_bookings",
    "avg_price_per_room": "avg_room_price",
    "no_of_special_requests": "special_request_count",
    "booking_status": "is_canceled"
})

df = df.drop(columns=["arrival_year", "arrival_month", "arrival_date", "Booking_ID"])

print(df.head())