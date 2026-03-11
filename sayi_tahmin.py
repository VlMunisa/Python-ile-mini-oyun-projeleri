import random

print("==== Sayi tahmin oyunu ====")
tahmin = 1

print("Bir sayi tuttum, hadi tahmin etmeye calis.")
sayi = random.randint(1,100)
while tahmin <= 7:
    sayi_tahmini = int(input(f"{tahmin}.Tahminin : "))

    if sayi_tahmini < sayi:
        print(f"{sayi_tahmini} : Daha buyuk sayi tuttum.")
    elif sayi_tahmini > sayi:
        print(f"{sayi_tahmini} : Daha kucuk sayi tuttum.")
    elif sayi_tahmini == sayi:
        print("Tebrikler, tuttugum sayiyi buldun.")
        break

    if tahmin == 7:
        print(f"Tahmin hakkin bitti. Tuttugum sayi {sayi}")
    tahmin += 1