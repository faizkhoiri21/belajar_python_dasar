#NESTED LIST

data_0 = [1,2,3]
data_1 = [3,4,5]

list_biasa = [1,2,3,4,5]
print(f"list biasa = {list_biasa}")

nested_list = [data_0, data_1]
print(f"nested list = {nested_list}")

peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Dedeh", 50, "Wanita"]

data_peserta = [peserta_0, peserta_1, peserta_2]
print(f"data peserta = {data_peserta}")

for peserta in data_peserta:
    print(f"\nnama = {peserta[0]}")
    print(f"umur = {peserta[1]}")
    print(f"gender = {peserta[2]}\n")

#dengan reference
list_copy = data_peserta.copy()
print(f"list copy = {list_copy}")
peserta_0[0] = "Bambang"
print(f"list copy = {list_copy}")
print(f"list = {data_peserta}")

