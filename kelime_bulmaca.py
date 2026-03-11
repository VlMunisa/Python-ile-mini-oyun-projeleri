import random

kelimeler = ["galatasaray", "kodlama", "kodmimari", "muhendis", "operator", "eren", "mauro", "icardi"]

gizli_kelime = random.choice(kelimeler)
tahmin = ["_"] * len(gizli_kelime)

hak = 7

print("=== Kelime tahmin oyunu ===")
print("Kelime : ", " ".join(tahmin))

while hak > 0 and "_" in tahmin:
    harf = input("Bir harf gir :").lower()

    if harf in gizli_kelime:
        for i in range(len(gizli_kelime)):
            if gizli_kelime[i] == harf:
                tahmin[i] = harf
        print("Dogru tahmin!")
    else:
        hak-=1
        print("Yanlis! Kalan hakkin", hak)
    print("Kelime : ", " ".join(tahmin))

if "_" not in tahmin:
    print("Tebrikler kelimeyi buldun!", gizli_kelime)
else:
    print("Tahmin etme hakkin bitti!!!")