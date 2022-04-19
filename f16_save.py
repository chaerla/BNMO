import os
from util import my_len
from util import find_path
from util import loadingmsg

# { I.S. : Diberikan input user, game, kepemilikan, dan riwayat yang bertipe tabel.  }
# { F.S. : Data pada data pada tabel user, game, kepemilikan, dan riwayat di-write pada folder yang diinput user }

# KAMUS
#   type tabel : array of array {tipe data bergantung pada masing-masing tabel yang sedang diakses}
#   { Variabel }
#   nama_folder : string
#   user, game, kepemilikan, riwayat : tabel

# { Fungsi dan Prosedur }
# procedure write_csv (input nama_folder : string, input arr_file : tabel, input nama_file: string)
# { I.S. : Diberikan input nama_folder yaitu folder penyimpanan, arr_file yaitu data yang ingin di-write pada file csv, nama_file yaitu nama file csv }
# { F.S. : Data pada arr_file di-write pada csv nama_file di folder nama_folder }
# function find_path (nama_folder: string) --> string
# { Input : fungsi find_path menerima input nama_folder yang bertipe string }
# { Output : fungsi find_path mengembalikan alamat directory tempat nama_folder ditemukan. Jika tidak ditemukan, mengembalikan string kosong atau "" }
# { Fungsi ini dispesifikasikan pada modul util }
# function my_len (arr: array) --> integer
# { Input : sebuah array }
# { Output : len array } 
# { Fungsi ini dispesifikasikan pada modul util }

# REALISASI FUNGSI DAN PROSEDUR 
# procedure write_csv (input nama_folder : string, input arr_file : tabel, input nama_file: string)
# KAMUS LOKAL
#   path_folder : string {Variabel yang menyatakan direktori/path folder}
#   f : SEQFILE of 
#       (*) arr_file
#       (1) mark
def write_csv (nama_folder, arr_file, nama_file):
    path_folder = find_path(nama_folder)
    # path_folder akan mengembalikan "" jika tidak nama_folder tidak ditemukan
    if(path_folder==""): # jika nama_folder tidak ditemukan
        path_folder = os.path.join(os.getcwd(), nama_folder)
        os.makedirs(path_folder) # buat folder tersebut
    path_file = os.path.join(path_folder, nama_file) 
    if (os.path.exists(path_file)): # jika file sudah ada dalam folder
        f = open(path_file, "w+") # overwrite
        for i in range (my_len (arr_file)):
            for j in range (my_len(arr_file[i])):
                f.write(str(arr_file[i][j]))
                if (j!=my_len(arr_file[i])-1):
                    f.write(";")
            f.write("\n")
        f.close()
    else: # jika file belum ada
        f = open(path_file, "x") # buat file tersebut
        for i in range (my_len (arr_file)):
            for j in range (my_len (arr_file[i])):
                f.write(str(arr_file[i][j]))
                if (j!=my_len(arr_file[i])-1):
                    f.write(";")
            f.write("\n")
        f.close()

# tes fungsi write_csv
# arr = [[0 for j in range (2)] for i in range (4)]
# nama_folder = input()
# nama_file = "kepemilikan.csv"
# arr = [["game_id", "user_id"]]
# write_csv(nama_folder, arr, nama_file)

# Fungsi save
def save (user, game, kepemilikan, riwayat):
    os.system('cls' if os.name=='nt' else 'clear')
    nama_folder = input("Masukkan nama folder penyimpanan: ")
    loadingmsg("Saving")
    write_csv (nama_folder, user, "user.csv")
    write_csv (nama_folder, game, "game.csv")
    write_csv (nama_folder, kepemilikan, "kepemilikan.csv")
    write_csv (nama_folder, riwayat, "riwayat.csv")
    print("Data telah tersimpan pada folder", nama_folder)
