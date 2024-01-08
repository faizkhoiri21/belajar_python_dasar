#OPERASI LIST

#count
data_angka = [1,3,5,4,3,5,3,9,8,9,6,8,3,4,5]
print(f"data angka = {data_angka}")

jumlah_3 = data_angka.count(3)
print(f"jumlah anhka 3 pada data = {jumlah_3}")
jumlah_9 = data_angka.count(9)
print(f"jumlah angka 9 pada data = {jumlah_9}")

#ambil posisi data (index)
data = ["Ucup", "Otong", "Dudung", "Yujeng"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
index_yujeng = data.index("Yujeng")
print(f"index dari Dudung adalah = {index_dudung}")
print(f"index dari Yujeng adalah = {index_yujeng}")

#Mengurutkan LIST
print(f"data angka sebelum diurutkan = {data_angka}")
data_angka.sort()
print(f"data angka setelah diurutkan = {data_angka}")
print(f"data sebelum diurutkan = {data}")
data.sort()
print(f"data setelah diurutkan = {data}")

#Membalik urutan
print(f"data angka dengan urutan benar = {data_angka}")
data_angka.reverse()
print(f"data angka dengan urutan terbalik = {data_angka}")
print(f"data dengan urutan benar = {data}")
data.reverse()
print(f"data dengan urutan terbalik = {data}")
