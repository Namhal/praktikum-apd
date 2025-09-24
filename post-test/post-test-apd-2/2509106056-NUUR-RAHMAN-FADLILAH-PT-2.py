# Variabel, memuat suhu dalam Celcius
suhu = (27, 33, 46, 55, 67, 92)

# Konversi suhu Celcius ke Fahrenheit
f1 = (9/5) * suhu[0] + 32
f2 = (9/5) * suhu[1] + 32
# Konversi suhu Celcius ke Kelvin
k1 = suhu[2] + 273.15
k2 = suhu[3] + 273.15
# Konversi suhu Celcius ke Reamur
r1 = (4/5) * suhu[4]
r2 = (4/5) * suhu[5]

#  Jumlah setiap suhu
jumlah = f1 + f2 + k1 + k2 + r1+ r2

# Rata-rata
rata2 = jumlah / len(suhu)

# Variabel NIM dan Boolean
NIM = 56
Bolean = NIM < rata2

# Output text
print("List suhu dalam Celcius :", suhu)
print ("Fahrenheit 1 :", f1)
print ("Fahrenheit 2 :", f2)
print ("Kelvin 1 :", k1)
print ("Kelvin 2 :", k2)
print ("Reamur 1 :", r1)
print ("Reamur 2 :", r2)
print ("Nim :", NIM)
print ("Bolean :", Bolean)
print ("Rata-rata :", rata2)
print ("Menampilkan slice index dari 46 sampai 96", suhu[-4:])