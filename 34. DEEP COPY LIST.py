#DEEP COPY LIST
print("DEEP COPY LIST")
print("\n")

data_0 = [1,2,3]
data_1 = [4,5,6]

data = [data_0, data_1, 10]
data_copy = data.copy()
print(f"data asli = {data}")
print(f"data copy = {data_copy}")
print("\n")

#address
print(f"address data asli = {hex(id(data))}")
print(f"address data copy = {hex(id(data_copy))}")
print("address berbeda")
print("\n")

#ubah data yang bukan list
print("kita ubah isi data copy yang bukan list")
data_copy[2] = 28
print(f"data asli = {data}")
print(f"data copy = {data_copy}")
print("ternyata bisa")
print("\n")

#address member 0
print(f"address member 0 data asli = {hex(id(data[0]))}")
print(f"address member 0 data copy = {hex(id(data_copy[0]))}")
print("teryata sama")
print("\n")

#deep copy list
print("untuk itu kita gunakan deep copy")
from copy import deepcopy
data_deepcopy = deepcopy(data)
print(f"data asli = {data}")
print(f"data copy = {data_copy}")
print(f"data deepcopy = {data_deepcopy}")
print("\n")

#address member 0
print(f"address member 0 data asli = {hex(id(data[0]))}")
print(f"address member 0 data copy = {hex(id(data_copy[0]))}")
print(f"address member 0 data deepcopy = {hex(id(data_deepcopy[0]))}")
print("address member pada  data deepcopy sudah berbeda dengan data asli")
print("\n")

#ubah member data deepcopy
data_deepcopy[0][0] = 2500
print(f"data asli = {data}")
print(f"data copy = {data_copy}")
print(f"data deepcopy = {data_deepcopy}")
print("ternyata jika member pada data deepcopy diubah, member data asli tidak terpengaruh")





