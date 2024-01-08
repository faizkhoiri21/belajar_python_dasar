print("====CONVERT FAHRENHEIT====")
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit = "))
print("Suhu =", fahrenheit, "F")

#CELCIUS
celcius = (5/9)*(fahrenheit-32)
print("suhu dalam celcius adalah", celcius, "C")

#REAMUR
reamur = (4/9)*(fahrenheit-32)
print("suhu dalam reamur adalah", reamur, "R")

#KELVIN
kelvin = ((5/9)*(fahrenheit-32))+273
print("suhu dalam kelvin adalah", kelvin, "K")
