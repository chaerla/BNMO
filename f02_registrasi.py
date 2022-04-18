#KAMUS
#data = array of array user.csv
#data = [["id","username","nama","password","role","saldo"],["a","b","c","d","e",3], ["a","b","c","d","e",3], ["a","ab","c","d","e",3]]

#UNTUK MEMEPERMUDAH AKSES
# 0 = id
# 1 = username
# 2 = nama
# 3 = password
# 4 = role
# 5 = saldo
from b01_Cipher import Enkripsi
from util import my_append,my_len
import os

#REGISTRASI
def FormulirRegistrasi(data):
  global namaPendaftar
  global usernamePendaftar
  global passwordPendaftar
  print('{:^120s}'.format("*"*120))
  namaPendaftar = input("Masukkan nama : ")
  usernamePendaftar = input("Masukkan username : ")
  passwordPendaftar = input("Masuukan password : ")
  PeriksaUsernameUnik(data, usernamePendaftar)

#PERIKSA usernamePendaftar ADAKAH YANG SAMA DENGAN yang di data
def PeriksaUsernameUnik(data, usernamePendaftar):
  for i in range (0, my_len(data)):
    if usernamePendaftar == data[i][1]: #2 untuk kolom username
      print("Username",usernamePendaftar, "sudah terpakai! Silahkan isi ulang form dengan username lain.")
      FormulirRegistrasi(data)
      break
    elif i == my_len(data) - 1 :
      PeriksaKetentuanUsername(usernamePendaftar)
      break

def GenerateIDPengguna(data):
  JumlahUser = 0
  for i in range (1, my_len(data)):
    temp=""
    for j in range (4):
      temp+=data[i][0][j]
    CurrID=""
    if(temp=="USER"):
      for k in range (4,7):
        CurrID += data[i][0][k]
    if (CurrID==""): CurrID="0"
  JumlahUser = int(CurrID)
  UserID = str(JumlahUser+1)
  for _ in range (3 - my_len(UserID)):
        UserID = "0" + str(UserID)
  return ("USER" + str(UserID))

#PENAMBAHAN PENGGUNA BARU DI TABEL DATA
def PemasukanDataPengggunaBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar):
  idPengguna = GenerateIDPengguna(data)
  data_baru = [idPengguna, usernamePendaftar, namaPendaftar, Enkripsi(passwordPendaftar), "user", 0]
  global dataBaru
  dataBaru = my_append(data, 6, data_baru)
  print()
  print('{:^120s}'.format("Registrasi akun "+usernamePendaftar+" berhasil!"))
  print()
  print('{:^120s}'.format("*"*120))
  #print(data)
  #user_id = data[idPengguna][0] #0 unutk kolom id 
  #rolePengguna = data[idPengguna][4] #4 untuk kolom role
  #print(user_id, rolePengguna)
  

#PERIKSA APAKAH usernamePendaftar SUDAH SESUAI KETENTUAN
def PeriksaKetentuanUsername(usernamePendaftar):
  usernameBenar = True
  i = 0
  while (i < my_len(usernamePendaftar)) and usernameBenar:
    if not((65 <= ord(usernamePendaftar[i]) <= 90) or (97 <= ord(usernamePendaftar[i]) <= 122) or (48 <= ord(usernamePendaftar[i]) <= 57) or (ord(usernamePendaftar[i])== 45) or (ord(usernamePendaftar[i]) == 95)):
      print("Username tidak sesuai dengan ketentuan.") 
      print("Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.")
      usenameBenar = False
      FormulirRegistrasi(data)
      break
    elif i == my_len(usernamePendaftar) - 1 and usernameBenar:
      PemasukanDataPengggunaBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar)
      break
    i = i + 1

#RANGKUMAN PROSEDUR & FUNGSI
def registrasi(user):
  os.system('cls' if os.name=='nt' else 'clear')
  global data
  data = user
  print('{:^120s}'.format("*"*120))
  print('{:^120s}'.format("Registrasi"))
  FormulirRegistrasi(data)
  return dataBaru
  #print(dataBaru)

# testing fungsi
# user = user = [["id","username","nama","password","role","saldo"],["ADMIN001", "admin", "admin", "admin", "admin", 999999], ["USER001", "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999], ["USER100", "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999]]
# Registrasi(user)
# print(dataBaru)
# print(PemasukanDataPengggunaBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar))
#print(data) masalah karena di global data kembali ke kondisi awal data (tanpa penambahan data dari registrasi)