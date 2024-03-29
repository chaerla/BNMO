#KAMUS
#data = array of array untuk user.csv

#untuk mempermudah akses array of array
#data = [["id","username","nama","password","role","saldo"],["a","b","c","d","e",3]]
# 0 = id
# 1 = usernmae
# 2 = nama
# 3 = password
# 4 = role
# 5 = saldo
import os
from b01_Cipher import Dekripsi
from util import my_len


#INPUT DARI PENGGUNA UNTUK LOG IN
def FormulirLogIn(data):
  global usernamePengguna
  global passwordPengguna
  print('{:^120s}'.format("*"*120))
  usernamePengguna = input("Masukkan username : ")
  passwordPengguna = input("Masukkan password : ")
  PencariUser(data, usernamePengguna)

#PENCARI NOMOR ID PENGGUNA DENGAN USERNAME PENGGUNA dari FormulirLogIn()
def PencariUser(data, usernamePengguna):
  for i in range (0, my_len(data)):
    if usernamePengguna == data[i][1]: #1 untuk username
      # i sebagai id pengguna
      if passwordPengguna == Dekripsi(data[i][3]): #3 unutk password
        os.system('cls' if os.name=='nt' else 'clear')
        print('{:^120s}'.format("*"*120))
        print('{:^120s}'.format("Selamat datang " + data[i][2]+"! Selamat menggunakan BNMO!"))
        print('{:^120s}'.format("*"*120))
        global ret
    #print(data[i][id], data[i][role])
        ret = (data[i][0], data[i][4]) #0 unutk id dan 4 untuk role 
      else :
        print("Password salah!")
        FormulirLogIn(data)
      break
    elif i == my_len(data) - 1:
      print ("Username tidak ditemukan. Silahkan coba lagi!")
      FormulirLogIn(data)
      break
  
#KONFIRMASI PEMILIK AKUN DENGAN PEMERIKSAAN PASSWORD DAN ID PENGGUNA dari PencariUser()

#RANGKUMAN PEOSEDUR DAN FUNGSI
def LogIn(data):
  print('{:^120s}'.format("Lakukan LogIn untuk menggunakan BNMO"))
  print()
  FormulirLogIn(data)
  return ret

# testing fungsi
# data = user = [["id","username","nama","password","role","saldo"],[1, "admin", "admin", "admin", "admin", 999999], [2, "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999]]
# LogIn (data)
# print(ret)