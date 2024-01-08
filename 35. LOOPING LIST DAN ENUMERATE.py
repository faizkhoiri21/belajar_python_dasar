#LOOPING LIST DAN ENUMERATE

#for loop
print("FOOR LOOP")
kumpulan_angka = [1,3,2,4,5,6,4,6,4,6,9]
for angka in kumpulan_angka :
    print(f"angka = {angka}")

peserta = ["Ucup", "Otong", "Dudung", "Yujeng", "Bambang"]
for nama in peserta :
    print(f"nama = {nama}")
print("\n")

#for loop and range
print("FOOR LOOP AND RANGE")
kumpulan_angka = [1,3,2,4,5,6,4,6,4,6,9]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
print("\n")

#while loop
print("WHILE LOOP")
kumpulan_angka = [1,3,2,4,5,6,4,6,4,6,9]
panjang = len(kumpulan_angka)
i = 0
while i < panjang :
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
print("\n")

#list comprehension
print("LIST COMPREHENSION")
kumpulan_angka = [1,3,2,4,5,6,4,6,4,6,9]
kumpulan_angka_kuadrat = [f**2 for f in kumpulan_angka]
print(f"kumpulan angka = {kumpulan_angka}")
print(f"kumpulan angka kuadrat = {kumpulan_angka_kuadrat}")
[print(f"data kuadrat = {f**2}") for f in kumpulan_angka] 
[print(f"angka = {i}") for i in kumpulan_angka]

data = ["Ucup", 1,2,4, "Otong"]
print("\n")
[print(f"data = {i}") for i in data]
print("\n")

#enumerate
data = ["Ucup", "Otong", 1,3,7, "Bambang"]
for index, kampang in enumerate(data):
    print(f"index = {index}, data = {kampang}")

