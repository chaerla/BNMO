from util import harga_to_int
import os

def ubahgame (game):
    os.system('cls' if os.name=='nt' else 'clear')
    print('{:^120s}'.format("*"*120))
    print('{:^120s}'.format("UBAH GAME"))
    print('{:^120s}'.format("*"*120))
    
    # meminta input dari user
    id_input = input("Masukkan ID game: ")
    game_input = input("Masukkan nama game: ")
    kategori_input = input("Masukkan kategori: ")
    tahun_input = input("Masukkan tahun rilis: ")
    harga_input = input("Masukkan harga: ")
    found = False
    for data in game:
        if (data[0] == id_input): # mengubah data game
            found = True
            if (game_input!=""): 
                data[1] = game_input
            if(kategori_input !=""): 
                data[2] = kategori_input
            if(tahun_input !=""): 
                data[3] = int(tahun_input)
            if(harga_input !=""): 
                data[4] = harga_to_int(harga_input)
            print("Data", data[0],"berhasil diubah.")
            break
    # jika game dengan id yang dimasukkan tidak ditemukan
    if (not(found)):
        print("Game dengan ID", id_input,"tidak ditemukan.")
    print('{:^120s}'.format("*"*120))
            
        