# Login
username_benar = "rahman"
password_benar = "056"

while True:
    login_ok = False
    while not login_ok:
        user = input("User :  ")
        if user.strip() == "":
            print("User kosong oi")
            continue
        
        passw = input("Pass : ")
        if passw.strip() == "":
            print("Pass kosong oi")
            continue
        
        if user != username_benar and passw == password_benar:
            print("User salah")
        elif user == username_benar and passw != password_benar:
            print("Pass salah")
        elif user != username_benar and passw != password_benar:
            print("User & pass salah")
        else:
            print("Login berhasil")
            login_ok = True

    # Inisialisasi stok darah tanpa dictionary
    A_plus = 0
    A_minus = 0
    B_plus = 0
    B_minus = 0
    AB_plus = 0
    AB_minus = 0
    O_plus = 0
    O_minus = 0

    while True:
        gol_ok = False
        while not gol_ok:
            gol = input("Golongan (A/B/AB/O): ").upper()
            if gol.strip() == "":
                print("Golongan kosong")
            elif gol in ["A", "B", "AB", "O"]:
                gol_ok = True
            else:
                print("Golongan salah, cuma A,B,AB,O")

        rh_ok = False
        while not rh_ok:
            rh = input("Rhesus (+/-): ").upper()
            if rh == "":
                print("Rhesus kosong")
            elif rh in ["+", "-"]:
                rh_ok = True
            else:
                print("Rhesus salah! Cuma + atau -")

        gol_isi = gol + rh

        jum_ok = False
        while not jum_ok:
            jum = input("Jumlah kantong: ")
            if jum.strip() == "":
                print("Jumlah kosong")
                continue
            if not jum.isdigit():
                print("Harus angka")
                continue
            jum = int(jum)
            if jum <= 0:
                print("Jumlah tidak boleh 0")
            else:
                jum_ok = True

        ml = jum * 500

        if gol_isi == "A+":
            A_plus += ml
        elif gol_isi == "A-":
            A_minus += ml
        elif gol_isi == "B+":
            B_plus += ml
        elif gol_isi == "B-":
            B_minus += ml
        elif gol_isi == "AB+":
            AB_plus += ml
        elif gol_isi == "AB-":
            AB_minus += ml
        elif gol_isi == "O+":
            O_plus += ml
        elif gol_isi == "O-":
            O_minus += ml

        print("Tambah", ml, "ml untuk", gol_isi)

        ulang_ok = False
        while not ulang_ok:
            ulang = input("Lagi? (Y/T): ").upper()
            if ulang == "":
                print("Jawab cuy Y/T")
            elif ulang in ["Y", "T"]:
                ulang_ok = True
            else:
                print("Cuma Y/T")

        if ulang == "T":
            break

    print("\nSTOK DARAH")
    total_all = A_plus + A_minus + B_plus + B_minus + AB_plus + AB_minus + O_plus + O_minus
    print("Total:", total_all, "ml")

    print("\nA:")
    print("  A+ :", A_plus, "ml")
    print("  A- :", A_minus, "ml")
    print("  Total A :", A_plus + A_minus, "ml")

    print("\nB:")
    print("  B+ :", B_plus, "ml")
    print("  B- :", B_minus, "ml")
    print("  Total B :", B_plus + B_minus, "ml")

    print("\nAB:")
    print("  AB+ :", AB_plus, "ml")
    print("  AB- :", AB_minus, "ml")
    print("  Total AB :", AB_plus + AB_minus, "ml")

    print("\nO:")
    print("  O+ :", O_plus, "ml")
    print("  O- :", O_minus, "ml")
    print("  Total O :", O_plus + O_minus, "ml")

    print("\nTerima kasih")

    prog_ok = False
    while not prog_ok:
        prog = input("Ulang program? (Y/T): ").upper()
        if prog == "":
            print("Jawab coy Y/T")
        elif prog in ["Y", "T"]:
            prog_ok = True
        else:
            print("Cuma Y/T")

    if prog == "T":
        print("Selesai")
        break
