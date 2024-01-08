#CONTINUE

print("CONTINUE")

angka = 0
print(f"angka sekarang --> {angka}")

while angka < 11:
    angka += 1
    print(f"angka sekarang --> {angka}")


    if angka == 5:
        continue
    
    print("whassap")

print("ketika angka 5, maka perintah print(whassap) tidak akan dieksekusi karena terdapat continue")
