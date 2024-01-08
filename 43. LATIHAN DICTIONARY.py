import datetime
import string
import random
#import os

#template dict mahasiswa
mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '000000',
    'sks' : 0,
    'lahir' : datetime.datetime(1111,1,1)
    }

data_mahasiswa = {}

while True :
    #os.system("cls")
    print(f"\n{'SELAMAT DATANG' : ^20}")
    print(f"{'DATA MAHASISWA' : ^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM : ")
    mahasiswa['sks'] = int(input("SKS : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (yyyy) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY : mahasiswa})

    print(f"\n{'KEY':<7} {'Nama':<20} {'NIM':<7} {'SKS':<4} {'Tanggal Lahir':<13}")
    print("-"*55)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<7} {NAMA:<20} {NIM:<7} {SKS:<4} {LAHIR:<13}")

    islanjut = input("\nMau tambah lagi ga bro (y/n) : ")
    if islanjut == "n":
        break

print("\nAkhir dari program, terima kasih")
        
        
        
    
                          
                          
                          
