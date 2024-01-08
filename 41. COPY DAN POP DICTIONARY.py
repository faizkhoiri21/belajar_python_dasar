print("="*20, "COPY DAN POP DICTIONARY", "="*20)
print("\n")

#copy dictionary
print("#copy dictionary")
temen_temen = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "mas asep si kasyeep",
    "ton" : "anton suroton"
    }

friends = temen_temen.copy()
print(f"temen_temen = {temen_temen}\n")
print(f"friends = {friends}\n")

friends.update({"cup" : "ucup si kwereeen"})
print(f"temen_temen = {temen_temen}\n")
print(f"friends = {friends}\n\n")

#pop dictionary
print("#pop dictionary")
masasep = friends.pop("sep")
print(f"mas asep = {masasep}\n")
print(f"friends = {friends}\n")
print("pop pada dictionary berfungsi untuk mentransfer data menggunakan key\n\n")

#popitem dictionary
print("#popitem dictionary")
data_terakhir = friends.popitem()
print(f"data terakhir = {data_terakhir}\n")
print(f"friends = {friends}\n")
print("popitem pada dictionary berfungsi untuk mentransfer data terakhir saja")



