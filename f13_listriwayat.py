
# array kepemilikan:
#       collumns 
# ro    0       1       
# 0     [[game_id,user_id].
# 1     [GAME001, luffy]]
# kepemilikan [0][1]

# array game:
#       c o l
# ro    0       1       2           3           4               5
#  0 [[id,   nama,  kategori,    tahun_rilis    ,harga      ,stok],
#  1 [GAME001,BNMO - Play Along With Crypto,Adventure,2022,100000,1].
#  2 [GAME002;Dasar Pemrograman;Coding;2022;0;10]]
import os

from util import konversi_harga
def list_riwayat (riwayat, username):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("RIWAYAT PEMBELIAN"))
    print('{:^120s}'.format("*"*120))
    # for i in range len(kepemilikan):
        # if (kepemilikan[i][1] == username):
            # game_id = kepemilikan[i][0]
    found = False
    print("Daftar game: ")
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    for data in riwayat:
        if (username == data[3]): # Jika user id pengguna yang sedang log in sama dengan user id pada riwayat
            if(game_cnt==0): # Cetak header tabel
                print('{:^120s}'.format("DAFTAR GAME YANG MEMENUHI KRITERIA PENCARIAN:"))
                print()
                print('{:^4s}'.format("NO."), end="")
                print('{:^12s}'.format("ID GAME")+"|",end="")
                print('{:^46s}'.format("NAMA GAME")+"|",end="")
                print('{:^20s}'.format("HARGA")+"|",end="")
                print('{:^20s}'.format("TAHUN RILIS")+"|")
                print("-"*120)
            found = True
            game_cnt+=1 # increment jumlah game yang ditemukan
            # Cetak data game
            print('{:^4s}'.format(str(game_cnt)+"."), end="")
            print('{:^12s}'.format(data[0])+"|",end="")
            print('{:^46s}'.format(data[1])+"|",end="")
            print('{:^20s}'.format(konversi_harga(data[2]))+"|",end="")
            print('{:^20s}'.format(str(data[4]))+"|",end="")
            print()
    if (not(found)):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk beli.")
        ###################################

# testing
# riwayat = [["id","nama","harga","user_id","tahun_rilis"],["GAME001","BNMO - Play Along With Crypto",100000,2,2022]]
# username = int(input("Masukkan username: "))
# list_riwayat (riwayat, username)
