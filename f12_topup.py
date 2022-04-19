# misalnya array user :

#       c o l l u m n s
# ro    0       1       2       3       4       5
# 0 [["id","username",  "nama",     "password", "role",     "saldo"],
# 1 [  1,     "admin",  "admin",    "admin"   , "admin",    999999  ]
# 2 [  2,    "luffy"   ,  "Monkey D. Luffy" ,   "iamsungod"   ,  "user"  , 999999 ]]


# maka, user[0] = ["id","username",  "nama",     "password", "role",     "saldo"] (baris ke-0)
# user[1] = [  1,     "admin",  "admin",    "admin"   , "admin",    999999  ] (baris ke-1)
# user[1][0] = 1 (baris ke-1, kolom ke-0)
# user[1][1] = "admin"
# user[2][1] = "luffy"
from util import harga_to_int
import os
# { Input : tabel user}
# { Output : tabel user yang terupdate berdasarkan perubahan saldo yang dilakukan. }

# KAMUS
# type tabel : array of array {tipe data pada array bergantung pada masing-masing kolom pada csv}
# {Variabel}
# username, saldo : string
# flag : boolean { Variabel untuk mengecek apakah username yang dimasukkan valid. }
# i : integer


# {Fungsi}
# function harga_to_int (saldo: integer) --> integer
# { Input : sebuah string yang mewakili saldo yang akan ditambahkan } 
# { Output : integer yang mewakili saldo yang akan ditambahkan }
# { Fungsi ini dibuat untuk menangani kasus jika input saldo menggunakan pemisah ribuan (mis. 100.000). Realisasi fungsi ini terdapat di modul util.}

def topup(user):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("TOPUP"))
    print('{:^120s}'.format("*"*120))
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")
    flag = False
    for data in user: # loop ini untuk mengiterasi semua baris dalam array user, artinya data = user[1], user[2], dst...
        if (data[1]==username): # data[1] maksudnya kolom ke 1 (kolom username), artinya disini kita ngecek apakah username pada baris tersebut sama dengan username input user
            if (data[5] + harga_to_int(saldo)<0):
                print("Masukan tidak valid.")
            elif ( harga_to_int(saldo)<0):
                print("Saldo", username, "berhasil dikurangi sebanyak",-harga_to_int(saldo))
                data[5]+=harga_to_int(saldo)
            else:
                print("Saldo sebesar",saldo,"berhasil ditambahkan ke user",username,"!")
                data[5]+=harga_to_int(saldo)
            flag = True
    if (not(flag)):
        print("Username", username, "tidak ditemukan")
    print("*"*120)


# tes fungsi
# user = [["id","username","nama","password","role","saldo"],[1, "admin", "admin", "admin", "admin", 999999], [2, "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999]]
# user = topup(user)
# print (user)