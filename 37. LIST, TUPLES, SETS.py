print("LIST, TUPLES, AND SETS")
print("\n")

#list
print("#list")
data = [1,2,3,4,5,6,7,8,9]
print(f"data = {data}")
print(f"data dengan index 1 = {data[1]}")
data[0] = 0
data.append(10) 
print(f"data setelah diubah = {data}")
for index, data in enumerate(data):
    print(f"index {index} = {data}")
print("list menggunakan kurung siku, isi data dapat dimanipulasi, memiliki index\n")

#tuples
print("#tuples")
data = (1,2,3,4,5,6,7,8,9)
print(f"data = {data}")
print(f"data dengan index 0 = {data[0]}")
#data.append(11) <- tidak dapat dilakukan pada tuples
print("tuples menggunakan kurung lengkung, isi data tidak dapat dimanipulasi, memiliki index\n")

#sets
print("#sets")
data = {1,2,3,4,5,6,7,8,9}
print(f"data = {data}")
#print(f"data index 0 = {data[0]}") <- tidak dapat dilakukan pada set
#data.append(10) <- tidak dapat dilakukan
#data[0] = 0 <- tidak dapat dilakukan
print("sets menggunakan kurung kurawa, isi data tidak dapat dimanipulasi, tidak memiliki index, set juga bisa disebut sebagai himpunan")
