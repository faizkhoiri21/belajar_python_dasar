salam = "assalamualaikum"
print("normal =", salam)

salam = "assalamualaikum".upper()
print("upper =", salam)

salam = "assalamualaikum".lower()
print("lower =", salam)

sist = "BAMBANG"
whatlower = sist.islower()
print("sist is lower =", whatlower)

sist = "BAMBANG"
whatupper = sist.isupper()
print("sist is upper =", whatupper)

title = "All Or Not Arsenal"
apkhya = title.istitle()
print("apa iya", title, "format bener =", apkhya)

lis = ['arsenal', 'mu', 'city', 'liverpool']
print(lis)
gabung = ','.join(lis)
print(gabung)

gabungg = 'x'.join(lis)
print(gabungg)

pisah = gabungg.split('x')
print(pisah)

header = "pendaftaran".center(20, "-")
print("'"+header+"'")

header = "pendaftaran".rjust(20, "x")
print("'"+header+"'")






