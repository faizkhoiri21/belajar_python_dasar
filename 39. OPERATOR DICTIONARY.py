#OPERATOR DICTIONARY
print("OPERATOR DICTIONARY\n")

data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}
print(f"data dict = {data_dict}\n")

#panjang dictionary
print("#panjang dictionary")
lendict = len(data_dict)
print(f"panjang dict = {lendict}\n")

#cek key exist atau tidak
print("#cek key exist atau tidak")
key = "cup"
checkkey = key in data_dict
print(f"apakah {key} ada di data dict : {checkkey}")
keyy = "kis"
checkkeyy = keyy in data_dict
print(f"apakah {keyy} ada di data dict : {checkkeyy}\n")

#mengakses value (read) dengan get
print("#mengakses value (read) dengan get")
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis"))
print(data_dict.get("kis", "data tidak ditemukan\n"))

#mengupdate data
print("#mengupdate data")
data_dict["cup"] = "ucup si kereeeen"
print(data_dict)
data_dict["bambang"] = "bambang si kumissss"
print(data_dict)

data_dict.update({"cup" : "ucup surucup"})
print(data_dict)
data_dict.update({"sep" : "mas asyep si kasyeeep"})
print(data_dict, "\n")

#menghapus data
print("#menghapus data")
del data_dict["bambang"]
print(data_dict)




