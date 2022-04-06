import argparse
import os
import sys
from util import loadingmsg
# from f03_login import login
from f12_topup import topup
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
        print('{:^80s}'.format("*"*80))
        print('{:^80s}'.format("Selamat Datang di BNMO!"))
        print('{:^80s}'.format("*"*80))
        print()
        ds = load(nama_folder)
        user = ds[0]
        game = ds[1]
        kepemilikan = ds[2]
        riwayat = ds[3]
        # login()
        perintah = input("Masukkan perintah: ")
        print()
        # while(perintah!="exit"):
            # if (perintah == "topup" and role == "admin"):
            # user = topup (user)
            # if (perintah == "save"):
               # save(user, game, kepemilikan, riwayat)
            # if (perintah=="tictactoe"):
               # tictactoe()
            # perintah = input("Masukkan perintah: ")
            # print()

