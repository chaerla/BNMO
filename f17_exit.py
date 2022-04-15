
print(">>> exit")

exit = False
pilih = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
if pilih == "y" or "Y":
    save_data = str(input("Masukkan nama folder penyimpanan: "))
    save_data(save) #maksud aku di sini bakal jalanin fungsi save dari modul 16
    exit = True # program akan keluar (exit)
elif pilih == "n" or "N":
    exit = True # tidak ada yang perlu disave
else:
    pilih = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))