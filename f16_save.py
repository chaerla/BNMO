import os
from util import my_len
from util import find_path
from util import loadingmsg

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
