#Latihan Perulangan

print("MEMBUAT SEGI3 MENGGUNAKAN FOR \n")

sisi = int(input("Masukkan jumlah baris : "))

#Dummy variable
count = 1

for i in range(sisi):
    print("x" *(count))
    count += 1

print("\n"*2)
print("MEMBUAT SEGI3 MENGGUNAKAN WHILE \n")

count = 1
while True :
    print("x" * count)
    count += 1

    if count>sisi :
        break

print("\n"*2)
print("MEMBUAT SEGI3 HANYA DENGAN RANGE GANJIL \n")

reng = int(input("Masukkan jumlah baris : "))

count = 1
while True :
    #Supaya print jika baris ganjil
    if (count%2):
        print("x" * count)
        count += 1
    #Supaya skip jika baris genap
    else :
        count += 1
        continue
        
        
    
    #Supaya berhenti jika count > baris
    if count > reng:
        break

print("\n"*2)
print("MEMBUAT SEGI3 SAMA KAKI HANYA DENGAN RANGE GANJIL \n")

rang = int(input("Masukkan jumlah baris: "))

count = 1
spasi = int(rang/2)

while True :
    if (count%2):
        print(" "*spasi, "+"*count)
        count += 1
        spasi -= 1
    else :
        count += 1
        continue

    if count > rang:
        break

print("\n"*2)
print("MEMBUAT KUPAT(TANPA TAHU) HANYA DENGAN RANGE GANJIL \n")

rang = int(input("Masukkan jumlah baris: "))

count = 1
spasi = int(rang/2)

while True :
    if (count%2):
        print(" "*spasi, "+"*count)
        count += 1
        spasi -= 1
    else :
        count += 1
        continue

    if count > rang:
        break

countt = count-2
spasii = 1
while True :
    if (countt%2):
        print(" "*spasii, "+"*countt)
        countt -= 1
        spasii += 1
    else :
        countt -= 1
        continue
    if countt<1:
        break
    
