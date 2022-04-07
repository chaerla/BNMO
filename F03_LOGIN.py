#KAMUS
#data = array of array untuk user.csv

#untuk mempermudah akses array of array
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


#INPUT DARI PENGGUNA UNTUK LOG IN
def FormulirLogIn():
  global usernamePengguna
  global passwordPengguna
  usernamePengguna = input("Masukkan username : ")
  passwordPengguna = input("Masukkan password : ")

#PENCARI NOMOR ID PENGGUNA DENGAN USERNAME PENGGUNA dari FormulirLogIn()
def PencariUser(usernamePengguna, data):
  for i in range (my_len(data) + 1):
    if usernamePengguna == data[i][username]:
      global idPengguna
      idPengguna = i
    elif i == my_len(data)and usernamePengguna != data[i][username]:
      #DIARAHKAN KE FormulirLogIn() atau FormulirRegistrasi()
      return False
  
#KONFIRMASI PEMILIK AKUN DENGAN PEMERIKSAAN PASSWORD DAN ID PENGGUNA dari PencariUser()
def KonfirmasiUser(passwordPengguna, data)
  if passwordPengguna == data[i][password]:
    return True
  else :
    return False