import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('HotelReservations.csv')

df['is_canceled'] = df['is_canceled'].map({'Not_Canceled': 0, 'Canceled': 1})
df = df.dropna(subset=['avg_room_price', 'is_canceled', 'meal_plan'])

#T-test
cancelled = df[df['is_canceled'] == 1]['avg_room_price']
not_cancelled = df[df['is_canceled'] == 0]['avg_room_price']

ttest_stat, ttest_p = stats.ttest_ind(cancelled, not_cancelled, equal_var=False)

group_means = df.groupby('is_canceled')['avg_room_price'].mean()
labels = ['No Cancelado', 'Cancelado']

plt.figure(figsize=(6, 4))
sns.barplot(x=labels, y=group_means.values, palette='Blues')
plt.title('Precio promedio por estado de cancelación')
plt.ylabel('avg_room_price')
plt.ylim(0, df['avg_room_price'].max()*1.1)
plt.text(0, group_means.values[0] + 5,
         f"T-test: t = {ttest_stat:.2f}, p = {ttest_p:.4f}", fontsize=9)
plt.text(1, group_means.values[1] + 5,
         f"p < 0.05 → diferencia significativa", fontsize=9)
plt.tight_layout()
plt.savefig("practica4_test_cancelacion.png")
plt.close()

#ANOVA
meal_groups = [group['avg_room_price'] for name, group in df.groupby('meal_plan')]
anova_stat, anova_p = stats.f_oneway(*meal_groups)

meal_means = df.groupby('meal_plan')['avg_room_price'].mean().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=meal_means.index, y=meal_means.values, palette='viridis')
plt.title('Precio promedio por tipo de meal_plan')
plt.ylabel('avg_room_price')
plt.xticks(rotation=45)
plt.text(0, meal_means.max()*1.02,
         f"ANOVA: F = {anova_stat:.2f}, p = {anova_p:.4f}", fontsize=9)
plt.text(0, meal_means.max()*0.96,
         "p < 0.05 → al menos un grupo es distinto", fontsize=9)
plt.tight_layout()
plt.savefig("practica4_test_meal_plan.png")
plt.close()

