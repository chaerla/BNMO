from util import my_lower, konversi_harga
import os

def search_game_toko (game):
    os.system('cls' if os.name=='nt' else 'clear')
    print("*"*120)
    print('{:^120s}'.format("CARI GAME DI TOKO"))
    print("*"*120)
    id_input = input("Masukkan ID game: ")
    game_input = input("Masukkan nama game: ")
    kategori_input = input("Masukkan kategori: ")
    tahun_input = (input("Masukkan tahun rilis: "))
    harga_input = (input("Masukkan harga: "))
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    data_cnt = 0
    print("*"*120)
    for data in game:
        if (not(game_input=="" and id_input =="" and harga_input=="" and kategori_input =="" and tahun_input =="") and(data[0] == id_input or id_input =="") and (my_lower(data[1]) == my_lower(game_input) or game_input =="") and (my_lower(data[2]) == my_lower(kategori_input) or kategori_input == "") and (tahun_input=="" or int(tahun_input) == data[3]) and (harga_input=="" or data [4])) or (game_input=="" and id_input =="" and harga_input=="" and kategori_input =="" and tahun_input =="" and data_cnt!=0):
            if(game_cnt==0):
                print('{:^120s}'.format("DAFTAR GAME YANG MEMENUHI KRITERIA PENCARIAN:"))
                print()
                print('{:^4s}'.format("NO."), end="")
                print('{:^12s}'.format("ID GAME")+"|",end="")
                print('{:^46s}'.format("NAMA GAME")+"|",end="")
                print('{:^20s}'.format("KATEGORI")+"|",end="")
                print('{:^16s}'.format("TAHUN RILIS")+"|",end="")
                print('{:^16s}'.format("HARGA")+"|")
                print("-"*120)
            game_cnt+=1
            if (game_cnt>0):
                print('{:^4s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^46s}'.format(data[1])+"|",end="")
                print('{:^20s}'.format(data[2])+"|",end="")
                print('{:^16s}'.format(str(data[3]))+"|",end="")
                print('{:^16s}'.format(konversi_harga(data[4]))+"|")
    if (game_cnt==0):
        print("Tidak ada game di toko yang memenuhi kriteria.")
    print("*"*120)
#fail, help

# testing
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# search_game_toko (game)
            
        