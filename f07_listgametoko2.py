from util import my_len

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
    print_game(arr, tanda)

def print_game(arr, tanda):
    # ini udah ada code buat print game dari kent jadi aku copas aja supaya sergama
    if (tanda == "" or tanda == "+"):
        for i in range (1, my_len(arr)):
            print('{:^3s}'.format(str(i)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^40s}'.format(arr[i][1])+"|",end="")
            print('{:^15s}'.format(arr[i][2])+"|",end="")
            print('{:^6s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^10s}'.format(str(arr[i][4]))+"|",end="")
            print()
    elif (tanda == "-"):
        j=1
        for i in range (my_len(arr)-1, 0, -1):
            print('{:^3s}'.format(str(j)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^40s}'.format(arr[i][1])+"|",end="")
            print('{:^15s}'.format(arr[i][2])+"|",end="")
            print('{:^6s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^10s}'.format(str(arr[i][4]))+"|",end="")
            print()
            j+=1

def list_game_toko(game):
    # minta input skema sorting dari user
    

    # jika skema kosong (skema==""), jalankan print_game(game)
    # else: 
    # slice skema dari chr ke 0 sampai char kedua dari belakang, tapi ga boleh pake slice python jadi coba implementasikan sendiri
    # char paling belakang dimasukin ke variabel tanda
    # jika skema valid, lakukan my_sort(game, tanda, indeks kolom harga/tahun)
    # jika tidak, print tidak valid. 
    
# buat ngetes
game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10], ["GAME003","DOTA2","Moba",2003,50000,10]]
list_game_toko(game)