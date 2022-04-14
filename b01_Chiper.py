def my_len(arr):
    len = 0
    for i in arr:
        len+=1
    return len 

#Menambah komponenen pada List
def appendList(arr, data_baru):
    n_eff = my_len(arr)+1
    arrtemp = [0 for i in range (n_eff)]
    for i in range (my_len(arr)):
      arrtemp[i]=arr[i]
    arrtemp[n_eff-1] = data_baru
    return arrtemp

#Mengubah List menjadi String
def ListKeString(list):
  string = list[0]
  for i in range (1, len(list)):
    string = string + list[i]
  return string

#password menjadi kata rahasia
def Enskripsi(kata):
  #KUNCI
  a = 43
  b = 19

  katabaru = []
  
  for i in range (my_len(kata)):
    if 65 <= ord(kata[i]) <= 90:
      x = ord(kata[i])
      y = ((a*x + 13 + b) % 26) + 65
      katabaru = appendList(katabaru, chr(y))
    elif 97 <= ord(kata[i]) <= 122:
      x = ord(kata[i]) - 32
      z = (a*x + 13 + b)/26
      y = ((a*x + 13 + b) % 26) + 97
      #print(kata[i], x, z, y, chr(y))
      katabaru = appendList(katabaru, chr(y))
    else:
      katabaru = appendList(katabaru, kata[i])
  
  katabaru = ListKeString(katabaru)
  return katabaru

# kata rahasia menjadi password
def Deskripsi(kata):
  #KUNCI
  a = 43
  b = 19

  katabaru = ""
  invers_a = 0
  tanda = 0

  for i in range (26):
    tanda = (a * i) % 26
    if tanda == 1:
      invers_a = i

  for i in range ( my_len(kata)):
    if 65 <= ord(kata[i]) <= 90:
      katabaru = katabaru + chr(((invers_a * ((ord(kata[i]) + 65 - b)) % 26)) + 65)
    elif 97 <= ord(kata[i]) <= 122:
      x = ord(kata[i]) - 32
      katabaru = katabaru + chr(((invers_a * ((x + 65 - b)) % 26)) + 97)
    else:
      katabaru = katabaru + kata[i]
  
  return katabaru
