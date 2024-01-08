#LOOPING DICTIONARY
print("==========LOOPING DICTIONARY==========\n")

temen_temen = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "mas asep si kasyeeep",
    "ton" : "anton surotoon"
    }
print(f"temen temen = {temen_temen}\n")

#first try looping
print("#first try looping")
for temen in temen_temen :
    print(temen)
print("kesimpulan : yang keluar key nya\n")

#operator untuk mengambil item/iterables
print("#operator untuk mengambil item/iterables")
keys = temen_temen.keys()
print(keys)
for key in temen_temen.keys():
    print(key)
for key in temen_temen.keys() :
    print(temen_temen.get(key))
values = temen_temen.values()
print(values)
for value in temen_temen.values():
    print(value)
item = temen_temen.items()
print(item)
for item in temen_temen.items():
    print(item)
for key, value in temen_temen.items():
    print(f"key : {key}, value : {value}")
