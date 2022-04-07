
# 0 [["id",                 "nama",                "kategori",  "tahun_rilis", "harga",     "stok"],
# 1 [  "GAME001", "BNMO - Play Along With Crypto",  "Adventure",  "2022"   ,      "100000",    "1"  ]
# 2 [  "GAME002",    "Dasar Pemrograman"   ,        "Coding" ,   "2022"   ,       "0"  ,      "10" ]]


# maka, game[0] = ["id", "nama", "kategori", "tahun_rilis", "harga", "stok"] (baris ke-0)
# game[1][0] = "GAME001" (baris ke-1, kolom ke-0)
# game[1][1] = "BNMO - Play Along With Crypto"
# game[2][1] = "Dasar Pemrograman"

# parameter dalam fungsi adalah game, karena kitaa pakai array game bukan user
def stok(game):
    id = str(input("Masukkan ID game: "))
    stok = int(input("Masukkan jumlah: "))
    found = False # boolean untuk ngecek game ada ga di daftar game
    for data in game: 
        if (data[0] == id): # data[0] menunjukkan kolom ke-0 yaitu kolom id game
            found = True 
            if stok < 0 and (-(stok)<data[5]):
                data[5] += stok
                print("Stok game",data[1], "berhasil dikurangi. Stok sekarang: ", data[5] )
            elif stok > 0 :
                data[5] += stok
                print("Stok game",data[1], "berhasil ditambahkan. Stok sekarang: ", data[5] )
            elif stok < 0 and (-(stok)) > data[5]:
                print("Stok game", id, " gagal dikurangi karena stok kurang. Stok sekarang: ", data[5], "( <",-stok,")")
            # disini codenya kurang, coba baca ulang spesifikasi. Ada beberapa kasus. :
            # if stok kurang dari stok game(data[5]), output pesan error (coba buat codenya)
            # elif stok < 0, dan > data[5], data[5]+=stok print stok dikurangi (baca di spek) (coba buat codenya)
            # elif stok > 0, data[5]+=stok, print stok ditambah (coba buat codenya)
    if (not(found)):
        print("Tidak ada game dengan ID tersebut!")
        # coba code disini buat tanganin kasus kalau game ga ada ditemukan di array game (baca spek)
    return game

# test fungsi
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# print(stok(game))