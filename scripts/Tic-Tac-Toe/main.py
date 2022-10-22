def check(m):
    if ( (m[0][0] == m[0][1] == m[0][2] != 0)
     or (m[1][0] == m[2][0] == m[0][0] != 0 )
     or (m[0][0] == m[1][1] == m[2][2] != 0)
     or (m[1][0] == m[1][2] == m[1][2] != 0)
     or (m[2][0] == m[2][1] == m[2][2] != 0) 
     or (m[0][1] == m[1][1] == m[2][1] != 0) 
     or (m[0][2] == m[1][2] == m[2][2] != 0)
     or (m[0][2] == m[1][1] == m[2][0] != 0) ):
        return 1
    else:
        return 0


def display(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j],end = "\t")
        print("\n")


a=input("Want to play tic-tac-toe?y/n: ")
if a== "y":
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while True:
        i,j= int(input("X: enter row no.")), int(input("enter column no."))
        m[i][j]="X"
        display(m)
        if check(m)== 1:
            print("Congratulations you won!")
            break

        i,j= int(input("O: enter row no.")), int(input("enter column no."))
        m[i][j]="O"
        display(m)
        if check(m)== 1:
            print("Congratulations you won!")
            break
else:
    print("Good Bye!")