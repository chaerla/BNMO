import argparse
import os
import sys
from util import loadingmsg, find_path, errormsg_admin, errormsg_user
from f03_login import LogIn
from f04_tambahgame import tambahgame
from f05_ubahgame import ubahgame
from f06_ubahstok import ubah_stok
from f08_beligame import BeliGame
from f09_listgame import list_game
from f10_searchid import search_game_id
from f11_searchtoko import search_game_toko
from f12_topup import topup
from f13_listriwayat import list_riwayat
from f15_load import load
from f16_save import save
from f17_exit import exit
from b03_tictactoe import tictactoe
from f02_registrasi import registrasi

if __name__ == "__main__":    
        ds = load()
        
        # MEMASUKKAN DATA HASIL LOAD KE DALAM ARRAY
        user = ds[0]
        game = ds[1]
        kepemilikan = ds[2]
        riwayat = ds[3]
        sudah_save = False

        # Pengguna "dipaksa" untuk melakukan login sebelum dapat menggunakan fitur-fitur BNMO

        ## LOGIN ##
        user_info = LogIn(user)
        user_id = user_info[0]
        role = user_info[1]

        ###### MEMULAI PERMINTAAN COMMAND ######
        print()
        print("Ketik help untuk mengakses daftar commands.")
        perintah = input(">>>")
        print()
        # print(user)
        while(perintah!="exit"):
            # PEMANGGILAN F02 - REGISTER
            if (perintah=="register"):
                if (role=="admin"): user = registrasi (user)
                else: errormsg_user()
            
            # PEMANGGILAN F04 - TAMBAH GAME
            elif (perintah=="tambah_game"):
                if (role=="admin"): game = tambahgame (game)
                else: errormsg_user()
            
            # PEMANGGILAN F05 - UBAH GAME
            elif (perintah == "ubah_game"):
                if (role=="admin"): game = ubahgame (game)
                else: errormsg_user()

            # PEMANGGILAN F06 - UBAH STOK
            elif (perintah=="ubah_stok"):
                if (role=="admin"): game = ubah_stok (game)
                else: errormsg_user()
            
            # PEMANGGILAN F08 - BELI GAME
            elif (perintah=="beli_game"):
                if (role=="user"): 
                    temp_arr = BeliGame (user, game, kepemilikan, riwayat, user_id)
                    user = temp_arr[0]
                    game = temp_arr[1]
                    kepemilikan = temp_arr[2]
                    riwayat = temp_arr[3]
                else: errormsg_admin()
            
            # PEMANGGILAN F09 - LIST GAME USER
            elif (perintah == "list_game"):
                if (role=="user"): list_game (game, kepemilikan, user_id)
                else: errormsg_admin()
            
            # PEMANGGILAN F10 - SEARCH GAME USER
            elif (perintah == "search_my_game"):
                if (role=="user"): search_game_id(game, kepemilikan, user_id)
                else: errormsg_admin()

            # PEMANGGILAN F11 - SEARCH GAME TOKO
            elif (perintah == "search_game_toko"):
                search_game_toko(game)
            
            # PEMANGGILAN F12 - TOP UP
            elif (perintah == "topup"):
                if (role=="admin"): user = topup (user)
                else: errormsg_user()

            # PEMANGGILAN F13 - LIST RIWAYAT
            elif (perintah == "riwayat"):
                if (role=="user"): list_riwayat (riwayat, user_id)
                else: errormsg_admin()

            # PEMANGGILAN F16 - SAVE
            elif (perintah == "save"):
               save(user, game, kepemilikan, riwayat)
               sudah_save = True

            # PEMANGGILAN B03 - TICTACTOE
            elif (perintah=="tictactoe"):
               tictactoe()
            # if (perintah=="lihat_game"):
                # lihat_game(game, kepemilikan, username)
            
            else:
                print()
                print("Maaf. perintah tidak dikenali. Ketik help untuk melihat daftar commands.")

            print()
            perintah = input(">>>")
            print()

        exit(sudah_save, user, game, kepemilikan, riwayat)
        

