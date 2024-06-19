#Kullanıcıdan iki sayı alıyorum
num1 = float(input("Birinci Sayıyı Giriniz: "))
num2 = float(input("İkinci Sayıyı Giriniz: "))

#Yapılacak işlemin seçilmesi
print("Yapılacak İşlemi Seçiniz: ")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

#Bu kısımda kullanıcı seçimini yapacak
choice = input("Seçiniz (1/2/3/4): ")

#4 İşlemin sonucunu hesaplayan alan
if choice == "1": #Eğer 1 numaralı işlem seçilirse
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == "2": #Eğer 2 numaralı işlem seçilirse
    print(f"{num1} - {num2} = {num1 + num2}")
elif choice == "3": #Eğer 3 numaralı işlem seçilirse
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice =="4": #Eğer 4 numaralı işlem seçilirse
    if num2 !=0: #Sıfır bölme kontrolü
        print(f"{num1} / {num2} =  {num1 / num2}")
    else:
        print("Hata: Bir sayı sıfıra bölünmez")
else:
    print("Geçersiz seçim")