from f16_save import save
from util import loadingmsg
from time import sleep

def exit(sudah_save, user, game, kepemilikan, riwayat):
    # Jika belum melakukan save sebelumnya
    if(not(sudah_save)):
        pilih = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
        while(pilih!="Y" and pilih!="y" and pilih!="N" and pilih!="n"):
            print("Maaf. Jawaban tidak dikenali. Isi dengan Y atau y untuk menyimpan file.")
            print("Isi dengan N atau n jika tidak ingin melakukan penyimpanan file.")
            pilih = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
        if pilih == "y" or pilih == "Y":
            save(user, game, kepemilikan, riwayat)
        else: print("Anda tidak melakukan penyimpanan file. Perubahan tidak tersimpan.")
    print()
    sleep(2)
    loadingmsg("Exiting")
    print('{:^120s}'.format("*"*120))
    print()
    print('{:^120s}'.format("Terima kasih telah menggunakan BNMO!"))
    print('{:^120s}'.format("""
                                     ____    _   _      __  __    U  ___ u 
                                  U | __")u | \ |"|   U|' \/ '|u   \/"_ \/ 
                                   \|  _ \/<|  \| |>  \| |\/| |/   | | | | 
                                    | |_) |U| |\  |u   | |  | |.-,_| |_| | 
                                    |____/  |_| \_|    |_|  |_| \_)-\___/  
                                   _|| \\_  ||   \\,-.<<,-,,-.       \\    
                                  (__) (__) (_")  (_/  (./  \.)     (__)   
    """))
    print('{:^120s}'.format("*"*120))
    
