import time

# prosedur untuk mencetak board tictactoe
def kerangajaib():
    print("kerangajaib")
    print("Apa pertanyaanmu?", end="")
    input()
    local_time = time.localtime()
    if local_time.tm_sec % 6 == 0 :
        print ("\nYa\n")
    elif local_time.tm_sec % 4 == 0 :
        print ("\nTidak\n")
    elif local_time.tm_sec % 2 == 0 :
        print ("\nBisa Jadi\n")
    elif local_time.tm_sec % 3 == 0 :
        print ("\nMungkin\n")
    elif local_time.tm_sec % 5 == 0 :
        print ("\nTentunya\n")
    elif local_time.tm_sec % 2 == 1 :
        print ("\nTidak mungkin\n")
    