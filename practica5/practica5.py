
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series:
    if isinstance(df[x].iloc[0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x: str, y: str) -> None:
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef']
    df.plot(x=x, y=y, kind='scatter')

    plt.plot(df[x], [coef.values[1] * val + coef.values[0] for val in fixed_x], color='red')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'practica5_grafico1.png')
    plt.close()

# Cargar dataset
df = pd.read_csv("HotelReservations.csv")

# Convertir la fecha a tipo datetime
df['arrival_date_full'] = pd.to_datetime(df['arrival_date_full'])

# Agrupar por fecha y obtener promedio de precio
df_by_price = df.groupby("arrival_date_full")[["avg_room_price"]].mean().reset_index()
df_by_price.columns = ['arrival_date_full', 'avg_room_price_mean']

# Crear columna de días desde la primera fecha
df_by_price['days_since_start'] = (df_by_price['arrival_date_full'] - df_by_price['arrival_date_full'].min()).dt.days

# Imprimir tabla y graficar regresión
linear_regression(df_by_price, "days_since_start", "avg_room_price_mean")
