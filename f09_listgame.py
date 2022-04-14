
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
def list_game (game, kepemilikan, user_id):
    # for i in range len(kepemilikan):
        # if (kepemilikan[i][1] == username):
            # game_id = kepemilikan[i][0]
    found = False
    print("Daftar game: ")
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    for data in kepemilikan:
        if (user_id == data[1]):
            found = True
            game_cnt+=1 # increment jumlah game yang ditemukan
            game_id = data[0]
            for data in game:
                if (game_id==data[0]):
                    print('{:^3s}'.format(str(game_cnt)+"."), end="")
                    print('{:^12s}'.format(data[0])+"|",end="")
                    print('{:^40s}'.format(data[1])+"|",end="")
                    print('{:^15s}'.format(data[2])+"|",end="")
                    print('{:^6s}'.format(str(data[3]))+"|",end="")
                    print('{:^10s}'.format(str(data[4]))+"|",end="")
            print()
    if (not(found)):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
        ###################################

# testing
# kepemilikan = [["game_id","user_id"], ["GAME001", "2"]]
# game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
#username = input("Masukkan username: ")
# list_game (game, kepemilikan, username)
