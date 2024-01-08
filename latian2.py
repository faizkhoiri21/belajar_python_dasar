nama_awal = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_awal + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

panjang = len(nama_lengkap)
print("panjang dari" + " " + nama_lengkap + " " + "=" + " " + str(panjang))

D = "d"
status = D not in nama_lengkap
print("karakter", D, "ada pada karakter", nama_lengkap, "=", status)

d = "ucup"
status = d in nama_lengkap
print("karakter", d, "ada pada karakter", nama_lengkap, "=", status)

#INDEX
print("index ke-0 dari", nama_lengkap, "adalah", str(nama_lengkap[0]))
print("index ke-6 dari", nama_lengkap, "adalah", str(nama_lengkap[6]))
print("index 0-3 dari", nama_lengkap, "adalah", str(nama_lengkap[0:4]))
print("index 1, 3, 5, 7, 9 dari", nama_lengkap, "adalah", str(nama_lengkap[1:11:2]))

print("item paling kecil", "=", min(nama_lengkap))
print("item paling besar", "=", max(nama_lengkap))

data = nama_lengkap
jumlah = data.count("u")
print("jumlah huruf 'u' pada", data, "adalah", jumlah)


