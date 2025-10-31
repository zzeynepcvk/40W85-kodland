import random

sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifre uzunluğunu giriniz: "))

sonuc = ""

for i in range(sifre_uzunlugu):
    sonuc += random.choice(sifre)       
    
print("Oluşturulan şifre: ", sonuc)