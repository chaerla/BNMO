# array untuk testing
# kepemilikan = [["game_id","user_id"], ["GAME001", 1]]
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,10,10]]
# data = [["id","username","nama","password","role","saldo"],[1, "admin", "admin", "admin", "admin", 999999], [2, "luffy", "Monkey D. Luffy", "iamsungod", "user", 999999]]
# riwayat = [["game_id", "nama", "harga", "user_id", "tahun_beli"], ["GAME001","BNMO - Play Along With Crypto", 100000, 1, 2022]]
# idPengguna = 2

#KAMUS
#idGameMasukan = input dari pengguna
#dataUser = array of array user.csv
#kepemilikan = array of array kepemilikan.csv
#game = array of array game.csv
#riwayat = array of array riwayat.csv

#idBeliGame = variabel untuk menyimpan baris game yang diinginkan pada game.csv
#idPengguna = dari nomor id pengguna dari user.csv
import time

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

#MASUKAN UNTUK MEMBELI GAME
def FormulirBeliGame():
  global idGameMasukan
  idGameMasukan = input(("Masukkan ID Game yang ingin dibeli: "))

def GetYear():
  waktu = time.strftime("%Y")
  print(waktu)

#CARI GAME DI toko.csv
def CariGame(dataUser, game, kepemilikan, riwayat, idPengguna, idGameMasukan):
  for i in range (my_len(game)):
    if idGameMasukan == game[i][0]: #0 adalah id pada game.csv\\
      global idBeliGame
      idBeliGame = i #idGameBeli variabel untuk menandai id (nomor) game pada game.csv
      if game[i][5] > 0:
        CekKepemilikan(dataUser, game, kepemilikan, riwayat, idPengguna, idGameMasukan, idBeliGame)
      else:
        print("Stok game habis")
      break
    elif i == my_len(game) - 1:
      print("Game tidak ditemukan")
      break

#CEK KEPEMILIKAN di kepemilikan.csv
def CekKepemilikan(dataUser, game, kepemilikan, riwayat, idPengguna, idGameMasukan, idBeliGame):
  for i in range (my_len(kepemilikan)):
    if idPengguna == kepemilikan[i][1] and idGameMasukan == kepemilikan[i][0]: # 0 untuk game_id dan 1 untuk user_id pada kepemilikan.csv
      print("Game",game[idBeliGame][1],"sudah dimilki")
    elif i == my_len(kepemilikan) - 1:
      ProsesBeli(dataUser, game, kepemilikan, riwayat, idGameMasukan, idBeliGame, idPengguna)

#PROSES BELI
def ProsesBeli(dataUser, game, kepemilikan, riwayat, idGameMasukan, idBeliGame, idPengguna):
  for i in range (my_len(dataUser)):
    if dataUser[i][0] == idPengguna :
      indeksPengguna = i
      break
  if dataUser[indeksPengguna][5] >= game[idBeliGame][4]:
    global ret 
    #5 untuk saldo di user.csv #4 untuk harga di game.csv
    ###PERUBAHAN SALDO
    dataUser[indeksPengguna][5] = dataUser[indeksPengguna][5] - game[idBeliGame][4]
    ###APPEND KEPEMILIKAN
    dataKepemilikanBaru = [idGameMasukan, idPengguna]
    kepemilikan = my_append(kepemilikan, 2, dataKepemilikanBaru)
    ###PERUBAHAN STOK di game.csv
    game[idBeliGame][5] = game[idBeliGame][5] - 1
    ###APPEND di riwayat.csv
    riwayat_baru = [idGameMasukan, game[idBeliGame][1], game[idBeliGame][4], idPengguna, int(time.strftime("%Y"))]
    riwayat = my_append(riwayat, 5, riwayat_baru)
    ret = [dataUser, game, kepemilikan, riwayat]
    print("Game",game[idBeliGame][1],"berhasil dibeli")
  else :
    print("Saldo Anda tidak cukup.")

def BeliGame(dataUser, game, kepemilikan, riwayat, idPengguna):
  print('{:^120s}'.format("*"*120))
  print('{:^120s}'.format("BELI GAME"))
  print('{:^120s}'.format("*"*120))
  global ret
  ret = [dataUser, game, kepemilikan, riwayat]
  FormulirBeliGame()
  CariGame(dataUser, game, kepemilikan, riwayat, idPengguna, idGameMasukan)
  return ret

# testing fungsi
# print(BeliGame(data, game, kepemilikan, riwayat, idPengguna))