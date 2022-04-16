import sys
import os
from util import my_len
from util import my_split


def find_path(nama_folder):
    path = ""
    for (root, dirs, files) in os.walk('.', topdown=True):
        if nama_folder in root:
            path = os.path.join(path, root)
            return path

def read_csv(nama_folder, cnt_kolom, nama_file):
    with open(os.path.join(nama_folder, nama_file)) as file:
        lines = file.readlines()
        res = ["" for _ in range (my_len(lines))]
        i = 0
        for line in lines:
            items = my_split(line, cnt_kolom)
            res[i] = items
            i+=1
        return res


def load(nama_folder):
    user = read_csv(find_path(nama_folder), 6, "user.csv")
    game = read_csv(find_path(nama_folder), 6, "game.csv")
    kepemilikan = read_csv(find_path(nama_folder), 2, "kepemilikan.csv")
    riwayat = read_csv(find_path(nama_folder), 5, "riwayat.csv")
    return [user, game, kepemilikan, riwayat]
    
# testing
# nama_folder=input()
# print(find_path(nama_folder))
# load(find_path(nama_folder))