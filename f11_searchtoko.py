def search_game_toko (game):
    print("search_game_at_store")
    id_input = input("Masukkan ID game: ")
    game_input = input("Masukkan nama game: ")
    kategori_input = input("Masukkan kategori: ")
    tahun_input = (input("Masukkan tahun rilis: "))
    harga_input = (input("Masukkan harga: "))
    game_cnt = 0 # Variabel untuk menyimpan jumlah game
    if (id_input != ""):
        game_cnt += 1
        for data in game:
            if (id_input==data[0]):
                print('{:^3s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^40s}'.format(data[1])+"|",end="")
                print('{:^15s}'.format(data[2])+"|",end="")
                print('{:^6s}'.format(str(data[3]))+"|",end="")
                print('{:^10s}'.format(str(data[4]))+"|",end="\n")
            print()
    elif (game_input != ""):
        game_cnt += 1
        for data in game:
            if (game_input==data[1]):
                print('{:^3s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^40s}'.format(data[1])+"|",end="")
                print('{:^15s}'.format(data[2])+"|",end="")
                print('{:^6s}'.format(str(data[3]))+"|",end="")
                print('{:^10s}'.format(str(data[4]))+"|",end="\n")
            print()
    elif (kategori_input != ""):
        game_cnt += 1
        for data in game:
            if (kategori_input==data[2]):
                print('{:^3s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^40s}'.format(data[1])+"|",end="")
                print('{:^15s}'.format(data[2])+"|",end="")
                print('{:^6s}'.format(str(data[3]))+"|",end="")
                print('{:^10s}'.format(str(data[4]))+"|",end="\n")
            print()
    elif (tahun_input != ""):
        game_cnt += 1
        for data in game:
            if (tahun_input==data[3]):
                print('{:^3s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^40s}'.format(data[1])+"|",end="")
                print('{:^15s}'.format(data[2])+"|",end="")
                print('{:^6s}'.format(str(data[3]))+"|",end="")
                print('{:^10s}'.format(str(data[4]))+"|",end="\n")
            print()
    elif (harga_input != ""):
        game_cnt += 1
        for data in game:
            if (harga_input==data[4]):
                print('{:^3s}'.format(str(game_cnt)+"."), end="")
                print('{:^12s}'.format(data[0])+"|",end="")
                print('{:^40s}'.format(data[1])+"|",end="")
                print('{:^15s}'.format(data[2])+"|",end="")
                print('{:^6s}'.format(str(data[3]))+"|",end="")
                print('{:^10s}'.format(str(data[4]))+"|",end="\n")
            print()
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria")
#fail, help

# testing
game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10]]
search_game_toko (game)
            
        