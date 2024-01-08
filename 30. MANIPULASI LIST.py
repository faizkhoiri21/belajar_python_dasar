print("MANIPULASI LIST", "\n")

#index  0(-3)   1(-2)     2(-1)
data = ["ucup", "otong", "dudung"]

#MENGAMBIL DATA DARI LIST BERDASARKAN INDEX
print("MENGAMBIL DATA DARI LIST BERDASARKAN INDEX", "\n")
data_pertama = data[0]
print(f"data pertama adalah {data_pertama}")
data_pertama_pake_min = data[-3]
print(f"data pertama = {data_pertama_pake_min}")
data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

#MENGHITUNG PANJANG DATA
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

#MENAMBAH DATA SESUAI POSISI
print(f"data sebelum ditambah = {data}")
data.insert(1, "opik")
print(f"data setelah ditambaaaah = {data}")

#MENAMBAH DATA DI AKHIR LIST
data.append("bambang")
print(f"data ditambah lagi = {data}")

#MENGUBAH DATA
data[-1] = "Pamungkas"
print(f"data setelah di ubah = {data}")

#MEREMOVE DATA
data.remove("Pamungkas")
print(f"data remove = {data}")

#MEREMOVE DATA DI AKHIR LIST
data_akhir = data.pop()
print(f"data akhir = {data}")
print(f"data akhir yang dihapus = {data_akhir}")

