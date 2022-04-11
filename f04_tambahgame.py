from util import my_append
from util import my_len

def tambahgame(game):
    # disini code buat input Masukkan nama game, masukkan kategori, etc.
        # contoh
    nama_game = input("Masukkan nama game: ")
        # dst ...
        # kalau yang inputnya integer, pake int(input()) yaa contohnya yang tahun rilis, harga, dan stok awal
    harga = int(input())
    # disini tangani kasus kalau ada informasi yang ga dimasukin atau kosong
    # while nama_game == "" or kategori == "" dst
    while(nama_game==""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        # disini code buat input Masukkan nama game, masukkan kategori, etc.
        nama_game = input("Masukkan nama game: ")
        # dst ...
    # cari id_game, ini agak ribet mikir logikanya jadi aku langsung code aja tar aku jelasin kalau meet
    temp = str(my_len(game))
    for _ in range (3 - my_len(temp)):
        temp = "0" + str(temp)
    id_game = "GAME" + str(temp)
    # masukkan semua elemen ke sebuah array
    data_baru = [id_game, nama_game, kategori, tahun_rilis, harga, stok_awal]
    # append array ke array game
    # append itu butuh 3 parameter, array game, jumlah kolom array, sama data baru yang ingin dimasukkan
    # array awal kita itu array game, terus jumlah kolom game itu ada 6, teruss data_baru itu yang mau ditambahin
    return my_append(game, 6, data_baru)


# test

# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# test = tambahgame(game)
# print (test)