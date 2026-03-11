import random
print("==== Tas-Kagit-Makas oyunu ====")
liste= ["tas", "kagit", "makas"]
while True:
    print("Cikmak icin 'q' tusuna basiniz.")
    secim = input("Tas - Kagit - Makas ? : ").lower()
    if secim == "q":
        break

    if secim not in  liste:
        print("Gecersiz secim.")

    bilg_secim = random.choice(liste)
    print(f"Benim secimim {bilg_secim}")

    if secim == bilg_secim:
        print("Berabere.")
    elif (secim == "tas" and bilg_secim == "makas") or (secim == "kagit" and bilg_secim == "tas") or (secim == "makas" and bilg_secim == "kagit"):
        print("Kazandin!")
    else:
        print("Ben kazandim! :)")
