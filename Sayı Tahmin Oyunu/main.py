import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım kaç denemede bulabileceksiniz?")

    tutulmus_sayi = random.randint(1, 100)

    tahmin_sayisi = 0
    while True:
        tahmin = int(input("Tahmininizi girin: "))
        tahmin_sayisi += 1

        if tahmin < tutulmus_sayi:
            print("Daha büyük bir sayı söyleyin.")
        elif tahmin > tutulmus_sayi:
            print("Daha küçük bir sayı söyleyin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmini yaptınız!")
            break

sayi_tahmin_oyunu()
