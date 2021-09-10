import random

rep = int(input("How many numbers you want to calculate: "))
ran = str(input("Write the range seperating with comma: "))
mean = float(input("What is the mean you  want to calculate: "))
x=0

rang = ran.split(",")
sayılar = list()

for i in rang:
    i = int(i)
    sayılar.append(i)

if mean > max(sayılar) or mean < min(sayılar):
    print("Mean cannot be bigger than max or smaller than min: ")

toplam = 0
z = (toplam/rep)
liste = list()

while z!= mean:
    for i in range(rep):
        sayı = random.randint(sayılar[0],sayılar[1])
        toplam = toplam + sayı
        z = (toplam/rep)
        liste.append(sayı)
        print(f"Toplam: {toplam}, Sayı: {sayı}, Mean: {z} ")
    if z != mean:
        print("Bu sefer olmadı!")
        toplam = 0
        liste = list()
        continue
    else:
        print("Sayılar: ", liste)
        print("İşlem tamamlandı!!!") 