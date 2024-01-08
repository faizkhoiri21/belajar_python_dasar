nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

jutaan = 2000000
format_str = f"jutaan = {jutaan:,}"
print(format_str)

desimal = 2005.12345
format_str = f"desimal = {desimal:.3f}"
print(format_str)

desimal = 2005.12345
format_str = f"desimal = {desimal:019.3f}"
print(format_str)

angkaplus = 125
angkamin = -126
plus = f"angka plus = {angkaplus:+.2f}"
minus = f"angka min = {angkamin:-d}"
print(plus)
print(minus)

persen = 0.045
format_persen = f"persen = {persen:.1%}"
print(format_persen)

harga = 12000
jumlah = 3
total = f"total = Rp {harga * jumlah:,.2f}"
print(total)

angka = 100
binary = f"bin = {bin(angka)}"
octal = f"oct = {oct(angka)}"
hexa = f"hex = {hex(angka)}"
print(binary)
print(octal)
print(hexa)


