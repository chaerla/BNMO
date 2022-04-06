import os
from time import sleep

# pseudolen
def my_len(arr):
    len = 0
    for i in arr:
        len+=1
    return len 

# fungsi untuk split string menjadi array dengan size kol
def my_split(string, kol):
    res = ["" for _ in range (kol)]
    temp = ""
    i = 0
    for chr in string:
        if (chr!=";" and chr!="\n"):
            temp+=chr
        else:
            try:
                res[i] = int(temp)
            except ValueError:
                res[i] = temp
            temp = ""
            i+=1
    return res

# fungsi yang mengembalikan path folder
def find_path(nama_folder):
    path = ""
    for (root, dirs, files) in os.walk('.', topdown=True):
        if nama_folder in root:
            path = os.path.join(path, root)
            return path
    return path

# append array ke array of array
def my_append(arr, kol, data_baru):
    n_eff = my_len(arr)+1
    arrtemp = [["" for j in range (kol)] for i in range (n_eff)]
    for i in range (my_len(arr)):
        for j in range (kol):
            arrtemp[i][j]=arr[i][j]
    arrtemp[n_eff-1] = data_baru
    return arrtemp

# print message bergerak
def loadingmsg(msg):
    msg = msg+'...'
    for i in range(len(msg)-3, len(msg)+1, 1):
        os.system('cls' if os.name=='nt' else 'clear')
        print (msg[:i])
        sleep(0.5)
