#PROGRAM LIST BUKU
list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input("Judul Buku \t: ")
    penulis = input("Nama Penulis \t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n")
    print("="*10,"DATA BUKU","="*10)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} |{buku[0]}\t|{buku[1]}")
    print("="*31)
    print("\n")

    islanjut = input("Apakah hendak menambahkan data buku baru? (y/n) : ")
    if islanjut == "y":
        continue
    elif islanjut == "n":
        break
    
print("PROGRAM SELESAI")


        
        
