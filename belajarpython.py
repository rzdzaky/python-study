import os
import math

def main():
    os.system("cls")
    menu = [
        "\nPilih Program yang Tersedia :",
        "1. Menghitung SPP",
        "2. CM ke Inchi Konverter",
        "3. Menghitung Luas Segitiga",
        "4. Menghitung Luas Lingkaran",
        "5. Keluar"
    ]
    for i in menu:
        print(i)
    pilih = input("Masukan Nomor Program yang Dipilih : ")
    pilih = int(pilih)

    if (pilih==1):
        os.system("cls")
        print("\nProgram Menghitung SPP")
        sarana = input("biaya sarana\t: ")
        spp_ttp = input("spp tetap\t: ")
        spp_var = input("spp var \t: ")
        sks = input("sks\t\t: ")
        sarana = float(sarana) * 0.5
        spp_ttp = float(spp_ttp)
        sks = int(sks)
        spp_var = float(spp_var) 

        spp_var_fix = spp_var * sks
        total = sarana + spp_ttp + spp_var_fix

        sarana = f"biaya Sarana\t\t: Rp.{sarana}"
        spp_ttp = f"spp tetap\t\t: Rp.{spp_ttp}"
        spp_var = f"spp variabel per sks\t: Rp.{spp_var}"
        sks = f"sks yang diambil\t: {sks} sks"
        spp_var_fix = f"total spp variabel\t: Rp.{spp_var_fix}"
        total = f"Total Biaya SPP\t: Rp.{total}"

        os.system("cls")
        print("\nHasil Perhitungan")
        print(sarana, "\n", spp_ttp, "\n",spp_var, "\n", sks,"\n", spp_var_fix,"\n", total )
        input("\nTekan enter untuk lanjut..")
        main()

    elif (pilih==2):
        os.system("cls")
        print("\nProgram Konversi Cm ke Inchi")
        cm = input("masukkan nilai (cm) : ")
        cm = int(cm)
        inch = 0.393
        inch = float(inch)

        konversi = cm * inch
        
        konversi = f"{cm}cm adalah {konversi}inch"
        os.system("cls")
        print("\nHasil Koversi")
        print(konversi)
        input("\nTekan enter untuk lanjut..")
        main()

    elif (pilih==3):
        os.system("cls")
        print("\nProgram Hitung Luas Segitiga")

    elif (pilih==4):
        os.system("cls")
        print("\nProgram Hitung Luas & Keliling Lingkaran")
        hitung = [
            "1. Luas",
            "2. Keliling",
            "3. Diameter berdasarkan luas"
        ]
        for i in hitung:
            print(i)
        pilih = input("Masukan Nomor Program yang Dipilih : ")
        pilih = int(pilih)
        
        if (pilih==1):
            os.system("cls")
            print("\nMenghitung luas lingkaran")
            r = input("Jari-jari\t: ")
            r = float(r)
            
            L = r*r*3.14
            
            os.system("cls")
            print("\nHasil perhitungan luas lingkaran")
            L = f"Luas = phi * {r} x {r} \nLuas = {L}"
            print(L)
            input("\nTekan enter untuk lanjut..")
            main()
            
        elif (pilih==2):
            os.system("cls")
            print("\nMenghitung keliling lingkaran")
            d = input("Diameter\t: ")
            d = float(d)
            
            K = d*3.14
            
            os.system("cls")
            print("\nHasil perhitungan keliling lingkaran")
            K = f"Keliling = phi x {d} \nKeliling = {K}"
            print(K)
            input("\nTekan enter untuk lanjut..")
            main()
            
        elif (pilih==3):
            os.system("cls")
            print("\nMencari diameter lingkaran berdasar luas")
            l = input("Luas\t: ")
            l = int(l)
            
            d1 = l/3.14
            D = math.sqrt(d1) * 2
            
            os.system("cls")
            print("\nHasil perhitungan diameter lingkaran berdasar luas")
            D = f"Diameter = {int(D)}"
            print(D)
            input("\nTekan enter untuk lanjut..")
            main()
            
        else:
            os.system("cls")
            print("\nnomor program tidak tersedia !")
            input()
            main()
            

    elif (pilih==5):
        os.system("cls")
        print("\nAnda Keluar Program, Terimakasih Sudah Menggunakan")
        input()
        os.system("cls")
        exit()
        
    else:
        os.system("cls")
        print("\nnomor program tidak tersedia !")
        input()
        main()

main()