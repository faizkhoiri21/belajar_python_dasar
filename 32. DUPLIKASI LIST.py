#DUPLIKASI LIST

a = ["Ucup", "Otong", "Yujeng"]
print(f"a = {a}")

b = a
print(f"b = {b}")

#Kita coba utak atik
a[0] = "Bambang"
print(f"a = {a}")
print(f"b = {b}")
b.reverse()
print(f"a = {a}")
print(f"b = {b}")

#Cek address
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

#copy list
c = a.copy()
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print("\nPEMBUKTIAN")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
c[0] = "Leonardo"
print("Setelah di utak-atik")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("Kesimpulannya dengan menggunakan .copy dapat membuat data yang sama dengan data yang disalin namun memiliki address yang berbeda, sehingga jika data salinan diubah isinya tidak akan mempengaruhi isi data awal yang disalin")

