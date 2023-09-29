import random

karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int (input("kaç haneli şifre olusturmak istersiniz?"))
sifre = ""
for i in range (uzunluk):
    sifre += random.choice(karakterler)
print(sifre)
