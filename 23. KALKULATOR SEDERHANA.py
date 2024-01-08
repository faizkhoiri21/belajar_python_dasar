#KALKULATOR SEDERHANA
print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"="+"\n")

angka_pertama = float(input("Masukkan angka pertama : "))
operator = input("Masukkan operator (+ atau - atau x atau /): ")
angka_kedua = float(input("masukkan angka kedua : "))

if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_pertama * angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_pertama / angka_kedua
    print(f"hasilnya adalah {hasil}")
else:
    print("masukin yg bener lah")
