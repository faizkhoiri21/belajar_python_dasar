#LATIHAN KOMPARASI DAN LOGIKA
inputuser = float(input("masukkan angka \nlebih dari 0 kurang dari 5 \natau \nlebih dari 8 kurang dari 11: "))
print()

#---0+++5---
isLebihdariNolKurangdari5 = (0<inputuser<5)
print("Lebih dari 0 Kurang dari 5  =", isLebihdariNolKurangdari5)

#---8+++11---
isLebihdari8Kurangdari11 = (8<inputuser<11)
print("Lebih dari 8 Kurang dari 11 =", isLebihdari8Kurangdari11)

isCorrect = (isLebihdariNolKurangdari5 or isLebihdari8Kurangdari11)
print("Angka yang anda masukkan :", isCorrect)
print()


#LATIHAN 2
input = float(input("masukkan angka kurang dari nol \natau \nlebih dari 5 kurang dari 8 \natau \nlebih dari 11: "))

#Kurang dari 0
isKurangdari0 = (input<0)
print("Kurang dari 0=", isKurangdari0)

#Lebihdari5Kurangdari8
isLebih5Kurang8 = (5<input<8)
print("Lebih dari 5, kurang dari 8=", isLebih5Kurang8)

#Lebihdari11
isLebihdari11 = (input>11)
print("Lebih dari 11=", isLebihdari11)

isBENER = (isKurangdari0 or isLebih5Kurang8 or isLebihdari11)
print("angka yang anda masukkan :", isBENER)
