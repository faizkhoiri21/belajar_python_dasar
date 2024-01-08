import datetime

mahasiswa1 = {
    "nama" : "Ucup Surucup",
    "nim" : "505638",
    "sks" : 140,
    "beasiswa" : False,
    "lahir" : datetime.datetime(1999,1,1)
    }

mahasiswa2 = {
    "nama" : "Otong Surotong",
    "nim" : "505639",
    "sks" : 100,
    "beasiswa" : False,
    "lahir" : datetime.datetime(1999,2,2)
    }

mahasiswa3 = {
    "nama" : "Mas Asep Si Kasyeeep",
    "nim" : "505640",
    "sks" : 56,
    "beasiswa" : True,
    "lahir" : datetime.datetime(1993,12,14)
    }

data_mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3
    }

print(f"{'Key':<6} {'Nama':<20} {'NIM':<6} {'SKS':<3} {'Beasiswa':<8} {'Tanggal Lahir':<10}")
print("-"*70)

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks"]
    BEA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<6} {NAMA:<20} {NIM:<6} {SKS:<3} {BEA:^8} {LAHIR:^10}")

