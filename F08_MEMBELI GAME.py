#KAMUS
#idGameMasukan = input dari pengguna
#dataUser = array of array user.csv
#kepemilikan = array of array kepemilikan.csv
#toko = array of array toko.csv



from util import my_len
from util import my_append

#MASUKAN UNTUK MEMBELI GAME
def FormulirBeliGame():
  global idGameMasukan
  idGameMasukan = input()

#CEK KEPEMILIKAN di kepemilikan.csv
def CekKepemilikan(kepemilikan, idGameMasukan):
  for i in range (my_len(kepemilikan) + 1):
    if idPengguna == kepemilikan[i][user_id] :
      if idGameMasukan == kepemilikan[i][game_id]: 
        punyaGame = 1
        #return False
        print("Game sudah dimilki")
      elif i = my_len(kepemilikan) and idGameMasukan != kepemilikan[i][game_id]:
        punyaGame = 0
        #return True or langsung ke 
        #ProsesBeli(parameter)
    elif i = my_len(kepemilikan):
      punyaGame = 0
      #return True or langsung ke 
      #ProsesBeli(parameter)

#CARI GAME DI toko.csv
def CariGame(toko, idGameMasukan):
  for i in range (my_len(toko)):
    if idGameMasukan == toko[game_id][game_id]:
      adaGameDiToko = 1
      #return True or langsung masuk ke 
      #CekKepemilikan(parameter)
    elif i == my_len(toko):
      adaGameDiToko = 0
      #return False
      print("Tidak ditemukan Game dengan ID MASUKAN")

#PROSES BELI
def ProsesBeli(dataUser, toko, idGameMasukan):
  if dataUser[id][saldo] >= toko[idGameMasukan][harga]:
    dataUser[id][saldo] = dataUser[id][saldo] - toko[idGameMasukan][harga]
    dataKepemilikanBaru = [idPengguna, idGameMasukan]
    my_append(kepemilikan, 2, dataKepemilikanBaru)
  else :
    print(f"Saldo {namaPengguna} tidak cukup.")

#REALISASI
#FormulirBeliGame()
#CariGame()
#if CekKepemilikan():
#  ProsesBeli()



#return False bisa diarahin ke fungsi yang lain