import os
import time
import os

def lcg (x):
    a = 7
    c = 3
    m = 19
    rand = (a*x + c) % m
    return rand

# prosedur untuk mencetak board tictactoe
def kerangajaib():
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("KERANG AJAIB"))
    print('{:^120s}'.format("*"*120))

    print("Selamat datang di kerang ajaib BNMO. Aku punya jawaban untuk semua pertanyaanmu! ")
    print ("Apa yang ingin Anda tanyakan?", end="")
    input()
    arr = ["Ya", "Tidak", "Bisa Jadi", "Mungkin", "Tentunya", "Tidak Mungkin", "YNTKS"]
    local_time = time.localtime()
    x = lcg(local_time.tm_sec)    
    print(arr[x%7])
