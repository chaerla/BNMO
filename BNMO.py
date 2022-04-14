import argparse
import os
import sys
from winreg import EnableReflectionKey
from util import loadingmsg
from b01_Cipher import Enkripsi
from f02_Registrasi import Registrasi
from f03_login import LogIn
from f04_tambahgame import tambahgame
from f06_ubahstok import ubah_stok
from f08_MembeliGame import BeliGame
from f09_listgame import list_game
from f12_topup import topup
from f13_listriwayat import list_riwayat
from f15_load import load
from f16_save import save
from b03_tictactoe import tictactoe
from util import find_path

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", type = str)
    args = parser.parse_args()
    nama_folder = args.nama_folder
    if(find_path(nama_folder)==""):
        print("Folder "+ nama_folder+  " tidak ditemukan.")
    else:
        loadingmsg("Loading")
        print()
        print('{:^120s}'.format("*"*120))
        print('{:^120s}'.format("Selamat Datang di BNMO!"))
        print('{:^120s}'.format("*"*120))
        print()
        ds = load(nama_folder)
        user = [["id","username",  "nama",     "password", "role",     "saldo"],[  1,     "admin",  "admin",   Enkripsi("admin")  , "admin",    999999  ] ]
        game = ds[1]
        kepemilikan = ds[2]
        riwayat = ds[3]

        # Pengguna "dipaksa" untuk melakukan login sebelum dapat menggunakan fitur-fitur BNMO
        ## LOGIN ##
        #user_info = LogIn(user)
        #user_id = user_info[0]
        #role = user_info[1]

        ###### MEMULAI PERMINTAAN COMMAND ######
        perintah = input("Masukkan perintah: ")
        print()
        # print(user)
        while(perintah!="exit"):
            # PEMANGGILAN F02 - REGISTER
            if (perintah=="register"):
                if (role=="admin"): user = Registrasi (user)
                else: print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")
            
            # PEMANGGILAN F04 - TAMBAH GAME
            if (perintah=="tambah_game"):
                if (role=="admin"): game = tambahgame (game)
                else: print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")
            
            # PEMANGGILAN F06 - UBAH STOK
            if (perintah=="ubah_stok"):
                if (role=="admin"): game = ubah_stok (game)
                else: print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")
            
            # PEMANGGILAN F08 - BELI GAME
            if (perintah=="beli_game"):
                if (role=="user"): 
                    temp_arr = BeliGame (user, game, kepemilikan, riwayat, user_id)
                    user = temp_arr[0]
                    game = temp_arr[1]
                    kepemilikan = temp_arr[2]
                    riwayat = temp_arr[3]
                else: print("Maaf, Anda tidak dapat mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh user.")
            
            # PEMANGGILAN F09 - LIST GAME USER
            if (perintah == "list_game"):
                if (role=="user"): list_game (game, kepemilikan, user_id)
                else: print("Maaf, Anda tidak dapat mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh user.")
            
            # PEMANGGILAN F12 - TOP UP
            if (perintah == "topup"):
                if (role=="admin"): user = topup (user)
                else: print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")

            # PEMANGGILAN F13 - LIST RIWAYAT
            if (perintah == "riwayat"):
                if (role=="user"): list_riwayat (riwayat, user_id)
                else: print("Maaf, Anda tidak dapat mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh user.")

            # PEMANGGILAN F16 - SAVE
            if (perintah == "save"):
               save(user, game, kepemilikan, riwayat)

            # PEMANGGILAN B03 - TICTACTOE
            if (perintah=="tictactoe"):
               tictactoe()
            # if (perintah=="lihat_game"):
                # lihat_game(game, kepemilikan, username)
            print()
            perintah = input("Masukkan perintah: ")
            print()
        

