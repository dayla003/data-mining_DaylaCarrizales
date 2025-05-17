from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import string
import os

def open_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        content = f.readlines()
    return " ".join(content)

frase = open_file("snoopy.txt")

frase = frase.lower()
frase = frase.translate(str.maketrans("", "", string.punctuation))

palabras = frase.split()


all_words = " ".join(palabras)

wordcloud = WordCloud(
    background_color="white",
    min_font_size=5,
    width=800,
    height=400
).generate(all_words)

os.makedirs("img", exist_ok=True)

plt.figure(figsize=(8, 4), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("practica9/word_cloud.png")
plt.close()

print("Nube de palabras creada")
