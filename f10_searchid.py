
# array kepemilikan:
#       collumns 
# ro    0       1       
# 0     [[game_id,user_id].
# 1     [GAME001, luffy]]
# kepemilikan [0][1]

# array game:
#       c o l
# ro    0       1       2           3           4               5
#  0 [[id,   nama,  kategori,    tahun_rilis    ,harga      ,stok],
#  1 [GAME001,BNMO - Play Along With Crypto,Adventure,2022,100000,1].
#  2 [GAME002;Dasar Pemrograman;Coding;2022;0;10]]
def search_game_id (game, kepemilikan, username):
    # for i in range len(kepemilikan):
        # if (kepemilikan[i][1] == username):
            # game_id = kepemilikan[i][0]
    found = False
    print("search my_game")
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = int(input("Masukkan Tahun Rilis Game: "))
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    for data in kepemilikan:
        if (username == data[1]):
            found = True
            game_cnt+=1 # increment jumlah game yang ditemukan
            if (tahun_rilis == ""):
                for data in game:
                    if (id_game==data[0]):
                        print('{:^3s}'.format(str(game_cnt)+"."), end="")
                        print('{:^12s}'.format(data[0])+"|",end="")
                        print('{:^40s}'.format(data[1])+"|",end="")
                        print('{:^15s}'.format(data[2])+"|",end="")
                        print('{:^6s}'.format(str(data[3]))+"|",end="")
                        print('{:^10s}'.format(str(data[4]))+"|",end="\n")
                print()
            elif (id_game == ""):
                for data in game:
                    if (tahun_rilis==data[3]):
                        print('{:^3s}'.format(str(game_cnt)+"."), end="")
                        print('{:^12s}'.format(data[0])+"|",end="")
                        print('{:^40s}'.format(data[1])+"|",end="")
                        print('{:^15s}'.format(data[2])+"|",end="")
                        print('{:^6s}'.format(str(data[3]))+"|",end="") #masalah lainnya dia gamau ngeread integer
                        print('{:^10s}'.format(str(data[4]))+"|",end="\n") #mau masukin else tapi malah ngeprint elsenya 3 kali
                print()
            elif (id_game == "" and tahun_rilis == ""):
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")#error
            else: #(tahun_rilis != "" and id_game != ""):
                for data in game:
                    if (id_game==data[0] and tahun_rilis==data[3]):
                        print('{:^3s}'.format(str(game_cnt)+"."), end="")
                        print('{:^12s}'.format(data[0])+"|",end="")
                        print('{:^40s}'.format(data[1])+"|",end="")
                        print('{:^15s}'.format(data[2])+"|",end="")
                        print('{:^6s}'.format(str(data[3]))+"|",end="")
                        print('{:^10s}'.format(str(data[4]))+"|",end="\n")
                print()

# testing
kepemilikan = [["game_id","user_id"], ["GAME001", "luffy"]]
game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
username = input("Masukkan username: ")
search_game_id (game, kepemilikan, username)
