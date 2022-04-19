import sys
import os
from util import my_len, my_split, loadingmsg, find_path
import argparse

# Fungsi Load
# { Input : file csv user.csv, game.csv, kepemilikan.csv, riwayat.csv
# Output : array of tabel yang memuat tabel user, game, kepemilikan, riwayat }

# KAMUS
# { Variabel }
# type tabel : array of array {tipe data pada array bergantung pada masing-masing kolom pada csv}
# user : tabel {array yang memuat data user}
# game : tabel {array yang memuat data game}
# kepemilikan : tabel (array yang memuat data kepemilikan)
# riwayat : tabel {array yang memuat data riwayat}
# nama_folder : string

# { Fungsi dan Prosedur }
# Semua fungsi dari import os dan import argparse terdefinisi
# function find_path (nama_folder:string) --> string
# { Input : nama_folder }
# { Output : path folder }
# function readcsv (nama_folder: string, cnt_kolom: int, nama_file: string) --> tabel
# { Input : nama_folder, cnt_kolom yaitu jumlah kolom dalam file csv, nama_file yaitu nama file csv}
# { Output : array yang memuat data dari csv }
# Function di bawah ini didefinisikan di modul util
# function my_len (arr : array) --> int
# function my_split (string: string, kol: int ) --> array
# procedure loadingmsg (input msg: string)

def read_csv(nama_folder, cnt_kolom, nama_file):
    # { Input : nama_folder, cnt_kolom yaitu jumlah kolom dalam file csv, nama_file yaitu nama file csv}
    # { Output : array yang memuat data dari csv }

    # KAMUS LOKAL
    # res : tabel {variabel bertipe tabel kosong yang memuat data dari csv}
    # i : integer
    # lines : string
    
    # { fungsi berikut terdefinisi di python}
    with open(os.path.join(nama_folder, nama_file)) as file:
        lines = file.readlines()
        # { inisialisasi sebuah variabel bertipe tabel kosong yang akan memuat data dari csv}
        res = ["" for _ in range (my_len(lines))]
        i = 0
        for line in lines:
            items = my_split(line, cnt_kolom)
            res[i] = items
            i+=1
        return res

# FUNGSI LOAD
def load():
    # { ARGPARSE NAMA FOLDER }
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument("nama_folder", type = str)
        args = parser.parse_args()
        nama_folder = args.nama_folder
    except: # { Error handling jika tidak diberikan nama folder }
        print("Anda tidak memberikan nama folder penyimpanan!")
        exit()
    if(find_path(nama_folder)==""):
        print("Folder "+ nama_folder+  " tidak ditemukan.")
        exit()
    else:
        loadingmsg("Loading")
        print()
        # { WELCOME MESSAGE }
        print('{:^120s}'.format("*"*120))
        print()
        print('{:^120s}'.format("Selamat Datang di BNMO!"))
        print('{:^120s}'.format("""
                                         ____    _   _      __  __    U  ___ u 
                                      U | __")u | \ |"|   U|' \/ '|u   \/"_ \/ 
                                       \|  _ \/<|  \| |>  \| |\/| |/   | | | | 
                                        | |_) |U| |\  |u   | |  | |.-,_| |_| | 
                                        |____/  |_| \_|    |_|  |_| \_)-\___/  
                                       _|| \\_  ||   \\,-.<<,-,,-.       \\    
                                      (__) (__) (_")  (_/  (./  \.)     (__)   
        """))
        print('{:^120s}'.format("*"*120))
        print()
    user = read_csv(find_path(nama_folder), 6, "user.csv")
    game = read_csv(find_path(nama_folder), 6, "game.csv")
    kepemilikan = read_csv(find_path(nama_folder), 2, "kepemilikan.csv")
    riwayat = read_csv(find_path(nama_folder), 5, "riwayat.csv")
    return [user, game, kepemilikan, riwayat]
    
# testing
# nama_folder=input()
# print(find_path(nama_folder))
# load(find_path(nama_folder))