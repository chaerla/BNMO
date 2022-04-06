import time

def check_full():
    for i in range (3):
        for j in range (3):
            if (papan[i][j]=='#'):
                return False
    return True

def print_board():
    print('{:^40s}'.format("-"*40))
    print("Status papan saat ini:")
    for i in range (3):
        for j in range (3):
            print('{:^3s}'.format(papan[i][j]), end="")
            if(j!=2): print("|", end="")
        print()
    print('{:^40s}'.format("-"*40))

def find_winner():
    # cek baris
    for i in range (3):
        if (papan[i][0]==papan[i][1]==papan[i][2] and papan[i][0]!='#'):
            return papan[i][0]
    
    # cek kolom
    for i in range (3):
        if (papan[0][i]==papan[1][i]==papan[2][i] and papan[0][i]!='#'):
            return papan[0][i]
    
    # cek diagonal
    if (papan[0][0]==papan[1][1]==papan[2][2] and papan[0][0]!='#'):
        return papan[0][0]

    if (papan[0][2]==papan[1][1]==papan[2][0] and papan[0][2]!='#'):
        return papan[0][2]
    
    return '#'

def cek_input():
    ro = int(input("Baris yang ingin diisi [1..3]: "))
    while(ro<1 or ro>3):
        print("Masukan salah! Baris yang valid bernilai 1-3.")
        ro = int(input("Baris yang ingin diisi [1..3]: "))
    col = int(input("Kolom yang ingin diisi [1..3]: "))
    while(col<1 or col>3):
        print("Masukan salah! Kolom yang valid bernilai 1-3.")
        col = int(input("Kolom yang ingin diisi [1..3]: "))
    return (ro,col)


def input_player(c):
    pos = cek_input()
    ro = pos[0]
    col = pos[1]
    while(papan[ro-1][col-1]=='X' or papan[ro-1][col-1]=='O'):
        print("Kotak sudah terisi. Silahkan pilih kotak lain.")
        pos = cek_input()
        ro = pos[0]
        col = pos[1]
    papan[ro-1][col-1] = c

def game_end():
    print('{:^40s}'.format("*"*40))
    print('{:^40s}'.format("Game berakhir"))
    print('{:^40s}'.format("*"*40))


def tictactoe():   
    global papan, won, isFull, move_cnt
    move_cnt = 0
    papan =[["#" for j in range (3)] for i in range (3)]
    won = '#'
    isFull = False
    print('{:^40s}'.format("*"*40))
    print('{:^40s}'.format("Selamat Bermain TicTacToe!"))
    print('{:^40s}'.format("*"*40))
    print("Legenda: ")
    print("Kosong: #")
    print("Pemain 1: X")
    print("Pemain 2: O")
    print("Kolom bernomor 1,2,3 dari kiri ke kanan.")
    print("Baris bernomor 1,2,3 dari atas ke bawah.")
    print_board()
    time.sleep(2)
    print("Memulai permainan",end="")
    for _ in range (3):
        print('.',end="")
        time.sleep(0.5)
    print()
    while(move_cnt!=9 and won =='#'):
        print("Giliran pemain X")
        input_player('X')
        move_cnt+=1
        print_board()
        won = find_winner()
        isFull = check_full()
        if (won=='X'):
            print("Pemain X menang!")
            game_end()
        elif (move_cnt==9 and won=='#'):
            print("X dan O tie. Tidak ada pemenang.")
            game_end()
        else:
            print("Giliran pemain O")
            input_player('O')
            move_cnt+=1
            print_board()
            won = find_winner()
            isFull = check_full()
            if (won=='O'):
                print("Pemain O menang!")
                game_end()
            elif (move_cnt==9 and won=='#'):
                print("X dan O tie. Tidak ada pemenang.")
                game_end()
