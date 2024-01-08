#list -> array, mengakses dengan
#menggunakan index

#memanggil data pada list menggunakan index
print("#memanggil data pada list menggunakan index")
data_list = ["Ucup", "Otong", "Dudung"]
print(f"data index 0 = {data_list[0]}\n")

#dictionary (dict) -> associative array
#identifier -> key

data_dict = {
    'key' : 'value',
    'cp' : 'ucup',
    'tg' : 'otong',
    'dg' : 'dudung',
    'nmbr' : 100,
    'list' : data_list
    }

#mangggil data pada dict
print("#manggil data pada dict")
print(f"manggil ucup : {data_dict['cp']}")
print(f"manggil otong : {data_dict['tg']}")
print(f"manggil dudung : {data_dict['dg']}")
print(f"manggil angka 100 : {data_dict['nmbr']}")
print(f"manggil data list : {data_dict['list']}")

