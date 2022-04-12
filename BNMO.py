import argparse
import os
import sys
from util import loadingmsg
from f03_login import LogIn
from f12_topup import topup
from f15_load import load
from f16_save import save
# from b03_tictactoe import tictactoe
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
        user = ds[0]
        game = ds[1]
        kepemilikan = ds[2]
        riwayat = ds[3]
        user_info = LogIn(user)
        user_id = user_info[0]
        role = user_info[1]
        # arrtemp = login()
        # user_id = arrtemp[0]
        # role = arrtemp[1]
        perintah = input("Masukkan perintah: ")
        print()
        # print(user)
        while(perintah!="exit"):
            # if (perintah=="register"):
                # register(user)
            if (perintah == "topup"):
                if (role=="admin"): user = topup (user)
                else: print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")
            # if (perintah == "save"):
               # save(user, game, kepemilikan, riwayat)
            # if (perintah=="tictactoe"):
               # tictactoe()
            # if (perintah=="lihat_game"):
                # lihat_game(game, kepemilikan, username)
            perintah = input("Masukkan perintah: ")
            print()
        

