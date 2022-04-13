#KAMUS
#data = array of array user.csv
#data = [["id","username","nama","password","role","saldo"],["a","b","c","d","e",3], ["a","b","c","d","e",3], ["a","ab","c","d","e",3]]

#UNTUK MEMEPERMUDAH AKSES
# 0 = id
# 1 = usernmae
# 2 = nama
# 3 = password
# 4 = role
# 5 = saldo

def my_append(arr, kol, data_baru):
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
  for i in range (1, my_len(data)):
    if usernamePendaftar == data[i][1]: #2 untuk kolom username
      print("Username",usernamePendaftar, "sudah terpakai! Silahkan isi ulang form dengan username lain.")
      FormulirRegistrasi(data)
      break
    elif i == my_len(data) - 1 :
      PeriksaKetentuanUsername(usernamePendaftar)
      break

#PENAMBAHAN PENGGUNA BARU DI TABEL DATA
def PemasukanDataPengggunaBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar):
  idPengguna = my_len(data)
  data_baru = [idPengguna, usernamePendaftar, namaPendaftar, passwordPendaftar, "user", 0]
  global dataBaru
  dataBaru = my_append(data, 6, data_baru)
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
def Registrasi(user):
  global data
  data = user
  print('{:^80s}'.format("*"*80))
  print('{:^80s}'.format("Registrasi"))
  FormulirRegistrasi(data)
  #print(dataBaru)

# testing fungsi
# user = user = [["id","username","nama","password","role","saldo"],[1, "admin", "admin", "admin", "admin", 999999], [2, "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999]]
# Registrasi(user)
# print(dataBaru)
#print(PemasukanDataPengggunaBaru(data, usernamePendaftar, namaPendaftar, passwordPendaftar))
#print(data) masalah karena di global data kembali ke kondisi awal data (tanpa penambahan data dari registrasi)