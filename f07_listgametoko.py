from util import my_len

# array game:
#       c o l
# ro    0       1       2           3           4               5
#  0 [[id,   nama,  kategori,    tahun_rilis    ,harga      ,stok],
#  1 [GAME001,BNMO - Play Along With Crypto,Adventure,2022,100000,1].
#  2 [GAME002;Dasar Pemrograman;Coding;2022;0;10]]
def my_sort (arr, tanda, kol):
    n = my_len(arr)
    for i in range (0, n):
        for j in range (0, n-i-1):
            if(j!=0):
                if (arr[j+1][kol]<arr[j][kol]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
    
    print_game(arr, tanda)

def print_game(arr, tanda):
    if (tanda == "" or tanda == "+"):
        for i in range (1, my_len(arr)):
            print('{:^3s}'.format(str(i)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^40s}'.format(arr[i][1])+"|",end="")
            print('{:^15s}'.format(arr[i][2])+"|",end="")
            print('{:^6s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^10s}'.format(str(arr[i][4]))+"|",end="")
            print()
    elif (tanda == "-"):
        j=1
        for i in range (my_len(arr)-1, 0, -1):
            print('{:^3s}'.format(str(j)+"."), end="")
            print('{:^12s}'.format(arr[i][0])+"|",end="")
            print('{:^40s}'.format(arr[i][1])+"|",end="")
            print('{:^15s}'.format(arr[i][2])+"|",end="")
            print('{:^6s}'.format(str(arr[i][3]))+"|",end="")
            print('{:^10s}'.format(str(arr[i][4]))+"|",end="")
            print()
            j+=1

def list_game_toko(game):
    skema = input("Skema sorting: ")
    if (skema==""):
        print_game(game)
    else:
        temp = ""
        for i in range (my_len(skema)-1):
            temp+=skema[i]
        tanda = skema[my_len(skema)-1]
        if(temp=="harga" and (tanda=="+" or tanda =="-")):
            my_sort(game, tanda, 4)
        elif (temp=="tahun" and (tanda=="+" or tanda =="-")):
            my_sort(game, tanda, 3)
        else:
            print ("Tidak valid")

game = [["id","nama","kategori","tahun_rilis","harga","stok"],["GAME001","BNMO - Play Along With Crypto","Adventure",2022,100000,1],["GAME002","Dasar Pemrograman","Coding",2022,0,10], ["GAME003","DOTA2","Moba",2003,50000,10]]
list_game_toko(game)