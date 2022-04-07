#KAMUS
#data = array of array untuk user.csv
#       c o l l u m n s
# ro    0       1       2       3       4       5
# 0 [["id","username",  "nama",     "password", "role",     "saldo"],
# 1 [  1,     "admin",  "admin",    "admin"   , "admin",    999999  ]
# 2 [  2,    "luffy"   ,  "Monkey D. Luffy" ,   "iamsungod"   ,  "user"  , 999999 ]]
id = 0
username = 1
nama = 2
password = 3
role = 4
saldo = 5


def my_append(arr, kol, data_baru):
    global arrtemp
    n_eff = my_len(arr) + 1
    arrtemp = [["" for j in range (kol)] for i in range (n_eff)]
    for i in range (my_len(arr)):
        for j in range (kol):
            arrtemp[i][j]=arr[i][j]
    arrtemp[n_eff-1] = data_baru
    return arrtemp

def my_len(arr):
    len = 0
    for i in arr:
        len+=1
    return len 

#INI CONTOH DATA
data = [[0 for i in range (6)] for i in range (6)]

#REGISTRASI
def FormulirRegistrasi():
  global namaPendaftar
  global usernamePendaftar
  global passwordPendaftar
  namaPendaftar = input("Masukkan nama : ")
  usernamePendaftar = input("Masukkan username : ")
  passwordPendaftar = input("Masuukan password : ")


#PERIKSA usernamePendaftar ADAKAH YANG SAMA DENGAN yang di data
def PeriksaUsernameUnik(usernamePendaftar, data):
  for i in range (my_len(data)):
    if usernamePendaftar == data[i][username]:
      print("Username sudah digunakan. Ulangi", namaPendaftar, "!")
      FormulirRegistrasi()
      #return False
      break
    else :
      # if (periksaKetentuanUsername(usernamePendaftar)) :
        # PemasukanDataUserBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar)
      # else :
        # print("Username tidak memenuhi ketentuan.")
        # FormulirRegistrasi()
      periksaKetentuanUsername(usernamePendaftar)
      #return True


#PERIKSA APAKAH usernamePendaftar SUDAH SESUAI KETENTUAN
def periksaKetentuanUsername(usernamePendaftar):
  KebenaranUsername = 0
  # bool flag = True
  # while (i < my_len(usernamePendaftar)) and flag:

  for i in range (my_len(usernamePendaftar)):
    # if not ((65 <= ord(usernamePendaftar[i]) <= 91) or (97 <= ord(usernamePendaftar[i]) <= 123) or (48 <= ord(usernamePendaftar[i]) <= 58)):
    # flag = False

  # return flag
    for j in range (65, 91):
      if usernamePendaftar[i] == chr(j):
        KebenaranUsername = KebenaranUsername + 1
        break
    for j in range (97, 123):
      if usernamePendaftar[i] == chr(j):
        KebenaranUsername = KebenaranUsername + 1
        break
    for j in range (48, 58):
      if usernamePendaftar[i] == chr(j):
        KebenaranUsername = KebenaranUsername + 1
        break
    if usernamePendaftar[i] == chr(95):
        KebenaranUsername = KebenaranUsername + 1
    if usernamePendaftar[i] == chr(j):
        KebenaranUsername = KebenaranUsername + 1

  if KebenaranUsername == my_len(usernamePendaftar):
    #PemasukanDataUserBaru()
    return True
  else :
    print("Username tidak memenuhi ketentuan.")
    FormulirRegistrasi()
    #return False 
    


#PENAMBAHAN PENGGUNA BARU DI TABEL DATA
def PemasukanDataUserBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar):
  data_baru = [my_len(data) + 1, usernamePendaftar, namaPendaftar, passwordPendaftar, "user", 0]
  data = my_append(data, 6, data_baru)


#REALISASI DATA
#FormulirRegistrasi(parameter)
#PeriksaUsernameUnik(parameter)
#if periksaKetentuanUsername(parameter):
#  PemasukanDataUserBaru(parameter)

def register (data):
  FormulirRegistrasi()
  PeriksaUsernameUnik()
  return data
