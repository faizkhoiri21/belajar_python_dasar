list_pemain_arsenal = []

while True :
    print("Masukkan data pemain Arsenal")
    nama_pemain = input("Nama pemain\t: ")
    kebangsaan = input("Kebangsaan\t: ")
    posisi = input("Posisi\t\t: ")
    no_punggung = int(input("Nomor punggung\t: "))
    print("\n")

    data_pemain = [nama_pemain, kebangsaan, posisi, no_punggung]
    list_pemain_arsenal.append(data_pemain)

    print("="*20, "LIST PEMAIN ARSENAL", "="*20)
    
    for index, data in enumerate(list_pemain_arsenal):
        print(f"{index+1}. {data[0]}, {data[1]}, {data[2]}, {data[3]}")

    print("="*61)
    
    islanjut = input("\nApakah ingin menambahkan lagi?(y/n)")
    if islanjut == "n" :
        break

print("\nTerima kasih telah mencoba program sederhana ini")
