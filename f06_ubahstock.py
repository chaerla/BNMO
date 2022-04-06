import os

# 0 [["id",                 "nama",                "kategori",  "tahun_rilis", "harga",     "stok"],
# 1 [  "GAME001", "BNMO - Play Along With Crypto",  "Adventure",  "2022"   ,      "100000",    "1"  ]
# 2 [  "GAME002",    "Dasar Pemrograman"   ,        "Coding" ,   "2022"   ,       "0"  ,      "10" ]]


# maka, user[0] = ["id", "nama", "kategori", "tahun_rilis", "harga", "stok"] (baris ke-0)
# user[1][0] = "GAME001" (baris ke-1, kolom ke-0)
# user[1][1] = "BNMO - Play Along With Crypto"
# user[2][1] = "Dasar Pemrograman"

def stock(id):
    id = str(input("Masukkan id game"))
    stok = int(input("Masukkan stok terbaru: "))
    for data in game: 
        if (data[0] == id): # data[0] menunjukkan kolom ke-0 yaitu kolom id game
            data[5] += stok
    return user 

