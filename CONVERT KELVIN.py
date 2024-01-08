print("====CONVERT KELVIN====")
kelvin = float(input("Masukkan suhu dalam kelvin = "))
print("Suhu =", kelvin, "K")

#CELCIUS
celcius = kelvin-273
print("suhu dalam celcius adalah", celcius, "C")

#REAMUR
reamur = (4/5)*(kelvin-273)
print("suhu dalam reamur adalah", reamur, "R")

#FAHRENHEIT
fahrenheit = ((9/5)*(kelvin-273))+32
print("suhu dalam fahrenheit adalah", fahrenheit, "F")
