import os
import math
import pygame
# import datetime
import time
import random
 
pygame.init()

def main():
    def waktu():
        time.localtime()
        string_waktu = time.strftime("Jam %H:%M:%S WIB | Tgl %m-%d-%Y")
        print(string_waktu)
        # while True:
        #     print(datetime.datetime.now().strftime("Jam %H:%M:%S WIB | Tgl %m-%d-%Y"), end="\r")
            # time.sleep(1)
        
    def menu_pertama():
        os.system("cls")
        print("\nProgram Menghitung SPP")
        sarana = float(input("biaya sarana\t: ")) * 0.5
        spp_ttp = float(input("spp tetap\t: "))
        spp_var = float(input("spp var \t: "))
        sks = int(input("sks\t\t: "))

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

    def menu_kedua():
        os.system("cls")
        print("\nProgram Konversi Cm ke Inchi")
        cm = int(input("masukkan nilai (cm) : "))
        inch = float(0.393)

        konversi = cm * inch
            
        konversi = f"{cm}cm adalah {konversi}inch"
        os.system("cls")
        print("\nHasil Koversi")
        print(konversi)
        input("\nTekan enter untuk lanjut..")
        main()

    def menu_ketiga():
        os.system("cls")
        print("\nBentuk Segitiga ke 1\n")
        a = 5
        for i in range(0, a):
            for j in range(0, i + 1):
                print('* ' , end='')
            print('')
        
        input("\nenter untuk bentuk selanjutnya..")
        
        os.system("cls")
        print("\nBentuk Segitiga ke 2\n")
        a = 6
        for i in range(0, a):
            for j in range(0, a - 1):
                print('* ' , end='')
            a -= 1
            print('')
        
        input("\nenter untuk bentuk selanjutnya..")
        
        os.system("cls")
        print("\nBentuk Segitiga ke 3\n")
        a = 5
        s = 2 * a - 2 # for spaces
        for i in range(0, a):
            for j in range(0, s):
                print(' ',end='')
            s -= 2
            for j in range(0, i + 1):
                print('* ', end='')
            print('')
        
        input("\nenter untuk bentuk selanjutnya..")
        
        os.system("cls")
        print("\nBentuk Segitiga ke 4\n")
        a = 5
        s = 0 # for spaces
        for i in range(0, a):
            for j in range(0, s):
                # print(j, end='')
                print(' ',end='')
            s += 2
            for j in range(0, a):
                print('* ' , end='')
            a -= 1
            print('')
            
        input("\nenter untuk bentuk selanjutnya..")
        
        os.system("cls")
        print("\nBentuk Segitiga ke 5\n")
        a = 5
        s = a - 1 # for spaces
        for i in range(0, a):
            for j in range(0, s):
                print(' ', end='')
            s -= 1
            for j in range(0, i + 1):
                print('* ', end='')
            print('')
        
        input("\nenter untuk bentuk selanjutnya..")
        
        os.system("cls")
        print("\nBentuk Segitiga ke 6\n")
        a = 5
        s = 0 # for spaces
        for i in range(0, a):
            for j in range(0, s):
                print(' ',end='')
            s += 1
            for j in range(0, a):
                print('* ' , end='')
            a -= 1
            print('')
        input("\nTekan enter untuk lanjut..")
        main()
    
    def menu_keempat():
        os.system("cls")
        print("\nProgram Hitung Lingkaran")
        hitung = [
            "Luas",
            "Keliling",
            "Diameter berdasarkan luas"
        ]
        for i, hitung in enumerate(hitung):
            print(i+1,hitung)
        pilih = int(input("Masukan Nomor Program yang Dipilih : "))
        
        if (pilih==1):
            os.system("cls")
            print("\nMenghitung luas lingkaran")
            r = float(input("Jari-jari\t: "))
            s = input("Satuan\t\t: ")
            
            L = r*r*3.14
            
            os.system("cls")
            print("\nHasil perhitungan luas lingkaran")
            L = f"Luas = phi * {r} x {r} \nLuas = {L}{s}"
            print(L)
            input("\nTekan enter untuk lanjut..")
            main()
            
        elif (pilih==2):
            os.system("cls")
            print("\nMenghitung keliling lingkaran")
            d = float(input("Diameter\t: "))
            s = input("Satuan\t\t: ")
            
            K = d*3.14
            
            os.system("cls")
            print("\nHasil perhitungan keliling lingkaran")
            K = f"Keliling = phi x {d} \nKeliling = {K}{s}"
            print(K)
            input("\nTekan enter untuk lanjut..")
            main()
        
        elif (pilih==3):
            os.system("cls")
            print("\nMencari diameter lingkaran berdasar luas")
            l = int(input("Luas\t: "))
            s = input("Satuan\t\t: ")
            
            d1 = l/3.14
            D = math.sqrt(d1) * 2
            
            os.system("cls")
            print("\nHasil perhitungan diameter lingkaran berdasar luas")
            D = f"Diameternya adalah {int(D)}{s}"
            print(D)
            input("\nTekan enter untuk lanjut..")
            main()
            
        else:
            os.system("cls")
            print("\nnomor program tidak tersedia !")
            input()
            main()
    
    def menu_kelima():        
        white = (0, 0, 0)
        black = (255, 255, 255)
    
        dis_width = 600
        dis_height = 400
        
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game By Rzdzaky')
        
        clock = pygame.time.Clock()
        
        snake_block = 10
        snake_speed = 10
        
        font_style = pygame.font.SysFont("", 25)#bahnschrift
        score_font = pygame.font.SysFont("", 25)#comicsansms
               
        def Your_score(score):
            value = score_font.render("Skor : " + str(score), True, black)
            dis.blit(value, [10, 10])
               
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
  
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 5.5, dis_height / 2.5])
                
        def gameLoop():
            game_over = False
            game_close = False
        
            x1 = dis_width / 2
            y1 = dis_height / 2
        
            x1_change = 0
            y1_change = 0
        
            snake_List = []
            Length_of_snake = 1
        
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        
            while not game_over:
 
                while game_close == True:
                    dis.fill(white)
                    message("Game Over! tekan C main lagi, tekan Q keluar", black)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()
        
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
        
                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(white)
                pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
                
                # for x in snake_List[:-1]:
                #     if x == snake_Head:
                #         game_close = True
                
                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)
        
                pygame.display.update()
        
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
        
                clock.tick(snake_speed)
        
            pygame.quit()
            main()
        
        gameLoop()
    
        
    def keluar():
        os.system("cls")
        print("\nAnda Keluar Program, Terimakasih Sudah Menggunakan")
        input()
        os.system("cls")
        exit()
        
    os.system("cls")
    waktu()
    print("\nPilih Program yang Tersedia :")
    menu = [
        "Menghitung SPP",
        "CM ke Inchi Konverter",
        "Bentuk Segitiga",
        "Rumus Lingkaran",
        "Snake Game",
        "Keluar"
    ]
    for i,menu in enumerate(menu):
        print(i+1,menu)
    pilih = input("Masukan Nomor Program yang Dipilih : ").lower()

    if (pilih == '1'):
        menu_pertama()

    elif (pilih=='2'):
        menu_kedua()

    elif (pilih=='3'):
        menu_ketiga()

    elif (pilih=='4'):
        menu_keempat()   
    
    elif (pilih=='5'):
        menu_kelima()  

    elif (pilih=='6'):
        keluar()
    
    elif (pilih=="r"):
        main()
        
    else:
        os.system("cls")
        print("\nnomor program tidak tersedia !")
        input()
        main()

main()