
# 0 [["id",                 "nama",                "kategori",  "tahun_rilis", "harga",     "stok"],
# 1 [  "GAME001", "BNMO - Play Along With Crypto",  "Adventure",  "2022"   ,      "100000",    "1"  ]
# 2 [  "GAME002",    "Dasar Pemrograman"   ,        "Coding" ,   "2022"   ,       "0"  ,      "10" ]]


# maka, game[0] = ["id", "nama", "kategori", "tahun_rilis", "harga", "stok"] (baris ke-0)
# game[1][0] = "GAME001" (baris ke-1, kolom ke-0)
# game[1][1] = "BNMO - Play Along With Crypto"
# game[2][1] = "Dasar Pemrograman"
import os

def ubah_stok(game):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("UBAH STOK GAME"))
    print('{:^120s}'.format("*"*120))
    id = str(input("Masukkan ID game: "))
    stok = int(input("Masukkan jumlah: "))
    found = False # Boolean untuk mengecek apakah id yang dimasukkan valid atau tidak
    for data in game: 
        if (data[0] == id): # data[0] menunjukkan kolom ke-0 yaitu kolom id game
            found = True 
            print()
            if stok < 0 and (-(stok)<data[5]):
                data[5] += stok
                print("Stok game",data[1], "berhasil dikurangi. Stok sekarang:", data[5] )
            elif stok > 0 :
                data[5] += stok
                print("Stok game",data[1], "berhasil ditambahkan. Stok sekarang:", data[5] )
            elif stok < 0 and (-(stok)) > data[5]:
                print("Stok game", id, " gagal dikurangi karena stok kurang. Stok sekarang:", data[5], "( <",-stok,")")
            print()
    if (not(found)):
        print()
        print("Tidak ada game dengan ID tersebut!")
        print()
    print('{:^120s}'.format("*"*120))
    return game

# test fungsi
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# print(stok(game))