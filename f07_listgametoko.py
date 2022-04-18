from util import my_len, konversi_harga
import os

# array game:
#       c o l
# ro    0       1       2           3           4               5
#  0 [[id,   nama,  kategori,    tahun_rilis    ,harga      ,stok],
#  1 [GAME001,BNMO - Play Along With Crypto,Adventure,2022,100000,1].
#  2 [GAME002;Dasar Pemrograman;Coding;2022;0;10]]

def my_sort (arr, tanda, kol):
    # coba buat skema sorting pakai bubble sort
    # hint : bandinginnya pake if arr[j][kol] >arr[j+1][kol]
    # kalau udah disort, print array game
    for i in range (my_len(arr)):
        for j in range (my_len(arr)-i-1):
            if (j!=0):
                if (arr[j+1][kol]<arr[j][kol]):
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
    print_game(arr, tanda)

def print_game(arr, tanda):
    print('{:^120s}'.format("DAFTAR GAME: "))
    print()
    print('{:^4s}'.format("NO."), end="")
    print('{:^12s}'.format("ID GAME")+"|",end="")
    print('{:^46s}'.format("NAMA GAME")+"|",end="")
    print('{:^20s}'.format("KATEGORI")+"|",end="")
    print('{:^16s}'.format("TAHUN RILIS")+"|",end="")
    print('{:^16s}'.format("HARGA")+"|")
    print("-"*120)
    # ini udah ada code buat print game dari kent jadi aku copas aja supaya sergama
    if (tanda == "" or tanda == "+"):
        for i in range (1, my_len(arr)):
            print('{:^4s}'.format(str(i)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^46s}'.format(arr[i][1])+"|",end="")
            print('{:^20s}'.format(arr[i][2])+"|",end="")
            print('{:^16s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^16s}'.format(konversi_harga(arr[i][4]))+"|",end="")
            print()
    elif (tanda == "-"):
        j=1
        for i in range (my_len(arr)-1, 0, -1):
            print('{:^4s}'.format(str(j)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^46s}'.format(arr[i][1])+"|",end="")
            print('{:^20s}'.format(arr[i][2])+"|",end="")
            print('{:^16s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^16s}'.format(str(arr[i][4]))+"|",end="")
            print()
            j+=1

def list_game_toko(game):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("LISTING GAME DI TOKO"))
    print('{:^120s}'.format("*"*120))
    skema = str(input("Masukkan skema sorting: "))

    # Buat sebuah temporary array yang merupakan copy dari array game. Array ini yang akan di-sort
    arr_temp = ["" for _ in range (my_len(game))]
    for i in range (my_len(game)):
        arr_temp[i] = game[i]

    if skema == "":
        print_game(game, "")
    else:
        temp = ""
        for i in range (my_len(skema)-1):
            temp+=skema[i]
        tanda = skema[my_len(skema)-1]
        if (temp == "harga"):
            my_sort(arr_temp, tanda, 4)
        elif (temp == "tahun"):
            my_sort(arr_temp, tanda, 3)
        else:
            print ("Skema sorting tidak valid.")
    print('{:^120s}'.format("*"*120))
# buat ngetes
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10], ["GAME003","DOTA2","Moba",2003,50000,10]]
# list_game_toko(game)
# print(game)