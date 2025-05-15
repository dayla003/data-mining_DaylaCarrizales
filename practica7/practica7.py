import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv('HotelReservations.csv')

label_encoder = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = label_encoder.fit_transform(df[col])

df = df.drop(columns=['arrival_date_full'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

k = 3

kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
kmeans.fit(X_scaled)
labels = kmeans.labels_

df['Cluster'] = labels

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

df['PCA1'] = components[:, 0]
df['PCA2'] = components[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='Set2')
plt.title('Clusters con K-Means (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.savefig('practica7_grafico1.png')
plt.close()

cluster_counts = df['Cluster'].value_counts().sort_index()
print("\nCantidad de reservas por clúster:")
for cluster_id, count in cluster_counts.items():
    print(f"  Clúster {cluster_id}: {count} reservas")
