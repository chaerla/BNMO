def ubahgame (game):
    id_input = input("Masukkan ID game: ")
    game_input = input("Masukkan nama game: ")
    kategori_input = input("Masukkan kategori: ")
    tahun_input = int(input("Masukkan tahun rilis: "))
    harga_input = int(input("Masukkan harga: "))
    for data in game:
        if (data[0] == id_input):
            if (game_input!=""): 
                data[1] = game_input
            elif (game_input==""): 
                data[1] = data[1]
            elif(kategori_input !=""): 
                data[2] = kategori_input
            elif (kategori_input==""): 
                data[2] = data[2]
            elif(tahun_input !=""): 
                data[3] = tahun_input
            elif (tahun_input==""): 
                data[3] = data[3]
            elif(harga_input !=""): 
                data[4] = harga_input
            elif (harga_input==""): 
                data[4] = data[4]
    return game
            
        