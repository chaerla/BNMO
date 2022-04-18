from util import my_append, my_len, harga_to_int
import os

def tambahgame(game):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("TAMBAH GAME KE TOKO"))
    print('{:^120s}'.format("*"*120))
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")
    
    while(nama_game=="") or (kategori=="") or (tahun_rilis=="") or (harga=="") or (stok_awal==""):
        # error handling jika ada input parameter yang kosong
        print()
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        print()
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
    
    # GENERATE ID GAME
    temp = str(my_len(game))
    for _ in range (3 - my_len(temp)):
        temp = "0" + str(temp)
    id_game = "GAME" + str(temp)
    # masukkan semua elemen data baru ke sebuah array
    data_baru = [id_game, nama_game, kategori, int(tahun_rilis), harga_to_int(harga), int(stok_awal)]
    print()
    print('{:^120s}'.format("Game "+nama_game+" berhasil ditambahkan!"))
    print('{:^120s}'.format("*"*120))
    print()
    # append array ke array game
    return my_append(game, 6, data_baru)


# test

# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# test = tambahgame(game)
# print(test)