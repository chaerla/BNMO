from util import my_append
from util import my_len

def tambahgame(game):
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = int(input("Masukkan tahun rilis: "))
    harga = int(input("Masukkan harga: "))
    stok_awal = int(input("Masukkan stok awal: "))
    
    while(nama_game=="") or (kategori=="") or (tahun_rilis=="") or (harga=="") or (stok_awal==""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = int(input("Masukkan tahun rilis: "))
        harga = int(input("Masukkan harga: "))
        stok_awal = int(input("Masukkan stok awal: "))
    # cari id_game, ini agak ribet mikir logikanya jadi aku langsung code aja tar aku jelasin kalau meet
    temp = str(my_len(game))
    for _ in range (3 - my_len(temp)):
        temp = "0" + str(temp)
    id_game = "GAME" + str(temp)
    # masukkan semua elemen ke sebuah array
    data_baru = [id_game, nama_game, kategori, tahun_rilis, harga, stok_awal]
    print('{:^120s}'.format("Game "+nama_game+" berhasil ditambahkan!"))
    # append array ke array game
    # append itu butuh 3 parameter, array game, jumlah kolom array, sama data baru yang ingin dimasukkan
    # array awal kita itu array game, terus jumlah kolom game itu ada 6, teruss data_baru itu yang mau ditambahin
    return my_append(game, 6, data_baru)


# test

# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# test = tambahgame(game)
# print(test)