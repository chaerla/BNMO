
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

def print_game(data, game_cnt):
    print('{:^3s}'.format(str(game_cnt)+"."), end="")
    print('{:^12s}'.format(data[0])+"|",end="")
    print('{:^40s}'.format(data[1])+"|",end="")
    print('{:^15s}'.format(data[2])+"|",end="")
    print('{:^6s}'.format(str(data[3]))+"|",end="")
    print('{:^10s}'.format(str(data[4]))+"|")

def search_game_id (game, kepemilikan, username):
    # for i in range len(kepemilikan):
        # if (kepemilikan[i][1] == username):
            # game_id = kepemilikan[i][0]
    found = False
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    found = False
    punya_game = False
    for data in kepemilikan:
        if (username == data[1]):
            punya_game = True
            if (tahun_rilis == "" and id_game !=""):
                for data_game in game:
                    if (id_game==data_game[0] and id_game == data[0]):
                        found = True
                        game_cnt+=1
                        print_game(data_game, game_cnt)
                print()
            elif (id_game == "" and tahun_rilis !=""):
                for data_game in game:
                    if (int(tahun_rilis)==data_game[3] and data[0] == data_game[0]):
                        found = True
                        game_cnt+=1
                        print_game(data_game, game_cnt)
                print()
            elif (tahun_rilis!="" and id_game!=""): #(tahun_rilis != "" and id_game != ""):
                for data_game in game:
                    if (id_game==data_game[0] and data[0] == data_game[0] and int(tahun_rilis)==data_game[3]):
                        found = True
                        game_cnt+=1
                        print_game(data_game, game_cnt)
                print()
            else:
                for data_game in game:
                    if (data[0] == data_game[0]):
                        print(data[0])
                        found = True
                        game_cnt+=1
                        print_game(data_game, game_cnt)
                print()
    
    if (not(found) and punya_game):
        print("Maaf. Tidak ada game pada inventory yang memenuhi kriteria.")
    if (not(punya_game)):
        print("Maaf. Inventory Anda kosong.")

# testing
# kepemilikan = [["game_id","user_id"], ["GAME001", "luffy"]]
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
# username = input("Masukkan username: ")
# search_game_id (game, kepemilikan, username)
