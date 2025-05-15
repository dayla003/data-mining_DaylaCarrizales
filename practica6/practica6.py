import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.decomposition import PCA


df = pd.read_csv('HotelReservations.csv')

label_encoder = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = label_encoder.fit_transform(df[col])

df = df.drop(columns=['arrival_date_full'])

X = df.drop(columns=['is_canceled'])  # Variable independiente
y = df['is_canceled']                 # Variable a predecir 0 = No Cancelado, 1 = Cancelado

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo KNN: {accuracy:.4f}')
print('\nReporte de clasificación:')
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

df_plot = pd.DataFrame(X_pca, columns=["PCA1", "PCA2"])
df_plot["is_canceled"] = y.values

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_plot, x="PCA1", y="PCA2", hue="is_canceled", palette="Set1")
plt.title("Distribución PCA de reservas por estado de cancelación")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.legend(title="Cancelación (0 = No, 1 = Sí)")
plt.grid(True)
plt.savefig("practica6_grafico1.png")
plt.close()
