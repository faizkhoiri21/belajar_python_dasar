#LIST
print("LISTTTTTT")
print("\n")

data_angka = [1,2,3,4,5,6,7,8,9,10]
print(data_angka)

data_string = ["ucup", "otong", "odah"]
print(data_string)

data_boolean = [True, False, True, True]
print(data_boolean)

data_campuran = [1, 4, "otong", False, 7, "ucup", True]
print(data_campuran)

print("\n", "CARA ALTERNATIF MENGGUNAKAN LIST")
data_range = range(1,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

print("\n", "LIST MENGGUNAKAN FOR")
list_pake_for = [i**2 for i in range(0, 10)] #** itu kuadrat
print(list_pake_for)

print("\n", "LIST MENGGUNAKAN FOR IF")
list_for_if = [i for i in range(0,13) if i%2 == 1] #ganjil
print(list_for_if)
