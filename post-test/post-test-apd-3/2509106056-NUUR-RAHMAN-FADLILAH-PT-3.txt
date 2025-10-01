# Login
# username == rahman
# password == 056

username = input("Masukkan Username : ")
password = input("Masukkan Password : ")

if username == "rahman" and password == "056":
    print("Selamat Login")
    login = True
elif username == "rahman" and password != "056":
    print("Password salah")
    login = False
elif password == "056" and username != "rahman":
    print("Username salah")
    login = False
else:
    print("Username dan Password salah")
    login = False

if login == True:
    print("MENU PILIHAN")
    print("1. Konversi panjang")
    print("2. Konversi massa")
    print("3. Konversi suhu")
    print("4. Konversi waktu")
    print("5. Konversi mata uang")
    print("6. Keluar")
    memilih = input("Masukkan Yang Mau Dipilih : ")

    if memilih == "1":
        print("KALKULATOR PANJANG")
        print("1. KAKI (FEET) KE METER")
        print("2. KILOMETER KE METER")
        print("3. CENTIMETER KE METER")
        rubah = input("PILIHAN (1-3) : ")
        angka = float(input("Masukkan angka : "))
        if rubah == "1":
            hasil = angka * 0.3048
            print("Hasilnya adalah : ", hasil)
        elif rubah == "2":
            hasil = angka * 1000
            print("Hasilnya adalah : ", hasil)
        elif rubah == "3":
            hasil = angka / 100
            print("Hasilnya adalah : ", hasil)
        else:
            print("Invalid")

    elif memilih == "2":
        print("KALKULATOR MASSA")
        print("1. PON (POUND KE KILOGRAM)")
        print("2. TON KE KILOGRAM")
        print("3. GRAM KE KILOGRAM")
        print("4. MILIGRAM KE KILOGRAM")
        print("5. DEKAGRAM KE KILOGRAM")
        rubah = input("PILIHAN : ")
        angka = float(input("Masukkan angka : "))
        if rubah == "1":
            hasil = angka * 0.453592
            print("Hasilnya adalah : ", hasil)
        elif rubah == "2":
            hasil = angka * 1000
            print("Hasilnya adalah : ", hasil)
        elif rubah == "3":
            hasil = angka / 1000
            print("Hasilnya adalah : ", hasil)
        elif rubah == "4":
            hasil = angka / 1000000
            print("Hasilnya adalah : ", hasil)
        elif rubah == "5":
            hasil = angka / 100
            print("Hasilnya adalah : ", hasil)
        else:
            print("Invalid")

    elif memilih == "3":
        print("KALKULATOR SUHU")
        print("1. CELCIUS KE KELVIN")
        print("2. FAHRENHEIT KE KELVIN")
        print("3. REAMUR KE KELVIN")
        rubah = input("PILIHAN : ")
        angka = float(input("Masukkan angka : "))
        if rubah == "1":
            hasil = angka + 273.16
            print("Hasilnya adalah : ", hasil)
        elif rubah == "2":
            hasil = (angka - 32) * 5/9 + 273.16
            print("Hasilnya adalah : ", hasil)
        elif rubah == "3":
            hasil = (angka * 5/4) + 273.16
            print("Hasilnya adalah : ", hasil)
        else:
            print("Invalid")

    elif memilih == "4":
        print("KALKULATOR WAKTU")
        print("1. MENIT KE DETIK")
        print("2. JAM KE DETIK")
        rubah = input("PILIHAN : ")
        angka = float(input("Masukkan angka : "))
        if rubah == "1":
            hasil = angka * 60
            print("Hasilnya adalah : ", hasil)
        elif rubah == "2":
            hasil = angka * 3600
            print("Hasilnya adalah : ", hasil)
        else:
            print("Invalid")

    elif memilih == "5":
        print("KALKULATOR MATA UANG")
        print("1. IDR KE USD")
        print("2. USD KE IDR")
        print("3. IDR KE JPY")
        print("4. JPY KE IDR")
        print("5. IDR KE EUR")
        print("6. EUR KE IDR")
        rubah = input("PILIHAN : ")
        angka = float(input("Masukkan angka : "))
        if rubah == "1":
            hasil = angka / 16600
            print("Hasilnya adalah : ", hasil)
        elif rubah == "2":
            hasil = angka * 16600
            print("Hasilnya adalah : ", hasil)
        elif rubah == "3":
            hasil = angka / 111
            print("Hasilnya adalah : ", hasil)
        elif rubah == "4":
            hasil = angka * 111
            print("Hasilnya adalah : ", hasil)
        elif rubah == "5":
            hasil = angka / 19500
            print("Hasilnya adalah : ", hasil)
        elif rubah == "6":
            hasil = angka * 19500
            print("Hasilnya adalah : ", hasil)
        else:
            print("Invalid")

    elif memilih == "6":
        print("Sesi berakhir")
    else:
        print("Invalid")
