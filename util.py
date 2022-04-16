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
    for i in range(len(msg)-3, len(msg)+1, 1):
        os.system('cls' if os.name=='nt' else 'clear')
        print (msg)
        msg+="."
        sleep(0.5)

def my_lower(string):
    ret = ""
    for i in range (my_len(string)):
        if (65 <= ord(string[i]) <= 90):
            ret += chr(ord(string[i]) + 32)
        else:
            ret += string[i]
    return ret

# fungsi mengubah harga ke integer. mis 100.000 menjadi 100000
def harga_to_int(harga):
    temp = ""
    for i in range (my_len(harga)):
        if(harga[i]!="."):
            temp+=harga[i]
    return int(temp)

# fungsi mengubah integer menjadi string dengan separator ribuan. mis 100000 menjadi 100.000
def konversi_harga(harga):
    temp = str(harga)
    ret = ""
    cnt = 1
    for i in range (my_len(temp)-1, -1, -1):
        ret = temp[i] + ret
        if(cnt%3==0) and i!=0:
            ret = "." + ret
        cnt+=1
    return ret

# error message untuk user
def errormsg_user():
    print("Maaf, Anda tidak memiliki izin untuk mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh administrator.")

# error message untuk admin
def errormsg_admin():
    print("Maaf, Anda tidak dapat mengakses perintah tersebut. Perintah tersebut hanya dapat diakses oleh user.")
