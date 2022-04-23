from util import my_len, konversi_harga
import os

# array game:
#       c o l
# ro    0       1       2           3           4               5
#  0 [[id,   nama,  kategori,    tahun_rilis    ,harga      ,stok],
#  1 [GAME001,BNMO - Play Along With Crypto,Adventure,2022,100000,1].
#  2 [GAME002;Dasar Pemrograman;Coding;2022;0;10]]

def my_sort (arr, tanda, kol):
    # Skema sorting yang digunakan adalah bubble sort
    # Hanya dilakukan satu kali sorting yaitu ascending (dari kecil ke besar)
    for i in range (my_len(arr)):
        for j in range (my_len(arr)-i-1):
            if (j!=0):
                if (arr[j+1][kol]<arr[j][kol]):
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
    print_game(arr, tanda)

# Procedure untuk mencetak array game
def print_game(arr, tanda):
    # parameter tanda untuk membedakan apakah dicetak secara ascending atau descending
    print('{:^120s}'.format("DAFTAR GAME: "))
    print()
    print('{:^4s}'.format("NO."), end="")
    print('{:^12s}'.format("ID GAME")+"|",end="")
    print('{:^46s}'.format("NAMA GAME")+"|",end="")
    print('{:^20s}'.format("KATEGORI")+"|",end="")
    print('{:^16s}'.format("TAHUN RILIS")+"|",end="")
    print('{:^16s}'.format("HARGA")+"|")
    print("-"*120)
    if (tanda == "" or tanda == "+"): # Cetak array secara ascending (dari depan ke belakang)
        for i in range (1, my_len(arr)):
            print('{:^4s}'.format(str(i)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^46s}'.format(arr[i][1])+"|",end="")
            print('{:^20s}'.format(arr[i][2])+"|",end="")
            print('{:^16s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^16s}'.format(konversi_harga(arr[i][4]))+"|",end="")
            print()
    elif (tanda == "-"): # Cetak array secara descending (dari belakang ke depan)
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
        print_game(game, "") # Jika skema kosong, maka langsung print array game awal, parameter tanda dibiarkan kosong
    else:
        temp = "" # temp adalah string untuk menentukan apakah skema adalah harga/tahun
        # slicing input skema dari user, ambil karakter pertama sampai kedua dari terakhir (karena jika input valid, karakter terakhir pastilah berupa tanda.)
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