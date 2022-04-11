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


#INPUT DARI PENGGUNA UNTUK LOG IN
def FormulirLogIn(data):
  global usernamePengguna
  global passwordPengguna
  usernamePengguna = input("Masukkan username : ")
  passwordPengguna = input("Masukkan password : ")
  PencariUser(data, usernamePengguna)

#PENCARI NOMOR ID PENGGUNA DENGAN USERNAME PENGGUNA dari FormulirLogIn()
def PencariUser(data, usernamePengguna):
  for i in range (1, my_len(data)):
    if usernamePengguna == data[i][1]: #1 untuk username
      # i sebagai id pengguna
      KonfirmasiUser(passwordPengguna, i)
      break
    elif i == my_len(data) - 1:
      print ("Username tidak ditemukan.")
      FormulirLogIn(data)
      break
  
#KONFIRMASI PEMILIK AKUN DENGAN PEMERIKSAAN PASSWORD DAN ID PENGGUNA dari PencariUser()
def KonfirmasiUser(passwordPengguna, i):
  if passwordPengguna == data[i][3]: #3 unutk password
    print("Log in berhasil")
    #print(data[i][id], data[i][role])
    return (data[i][0], data[i][4]) #0 unutk id dan 4 untuk role 
  else :
    print("Password salah!")
    FormulirLogIn(data)

#RANGKUMAN PEOSEDUR DAN FUNGSI
def LogIn(data):
  FormulirLogIn(data)

LogIn(data)