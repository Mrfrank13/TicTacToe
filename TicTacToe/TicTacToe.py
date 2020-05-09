board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#print(board)
import random
import time
import os
print('Computer Plays First\n')
while(1):
    os.system('cls')
    print('\t0\t\t1\t\t2')
    print()
    print('\t\t|\t\t|')
    print('0\t',board[0][0],'\t|\t',board[0][1],'\t|\t',board[0][2])

    print('    ____________|_______________|_____________')
    print('\t\t|\t\t|')
    print('1\t',board[1][0],'\t|\t',board[1][1],'\t|\t',board[1][2])
    print('    ____________|_______________|_____________')
    print('\t\t|\t\t|')
    print('2\t',board[2][0],'\t|\t',board[2][1],'\t|\t',board[2][2])
    print('\t\t|\t\t|')
    if((board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O' ) or
       (board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O' ) or
       (board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O' ) or
       (board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O' ) or
       (board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O' ) or
       (board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O' ) or
       (board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O' ) or
       (board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O' )):
        print('!!!YOU Win!!!')
        time.sleep(4)
        break
    print('\nComputers Turn\n')
    while(1):
        if((board[0][0]=='X' or board[0][0]=='O') and (board[0][1]=='X' or board[0][1]=='O') and (board[0][2]=='X' or board[0][2]=='O') and (board[1][0]=='X' or board[1][0]=='O') and (board[1][1]=='X' or board[1][1]=='O') and (board[1][2]=='X' or board[1][2]=='O') and (board[2][2]=='X' or board[2][2]=='O') and (board[2][1]=='X' or board[2][1]=='O') and (board[2][0]=='X' or board[2][0]=='O')):
            print('\nIts a Tie, Lets try again\n')
            board=[['',' ','  '],['  ',' ',''],['   ','    ','']]
            time.sleep(2)
            os.system('cls')
            print('\t0\t\t1\t\t2')
            print()
            print('\t\t|\t\t|')
            print('0\t',board[0][0],'\t|\t',board[0][1],'\t|\t',board[0][2])

            print('    ____________|_______________|_____________')
            print('\t\t|\t\t|')
            print('1\t',board[1][0],'\t|\t',board[1][1],'\t|\t',board[1][2])
            print('    ____________|_______________|_____________')
            print('\t\t|\t\t|')
            print('2\t',board[2][0],'\t|\t',board[2][1],'\t|\t',board[2][2])
            print('\t\t|\t\t|')
        rowchoice=[0,1,2]
        columnchoice=[0,1,2]
        row=random.choice(rowchoice)
        column=random.choice(columnchoice)
        if(board[row][column]!='X' and board[row][column]!='O'):
            board[row][column]='X'
            break
    time.sleep(2)
    os.system('cls')
    print('\t0\t\t1\t\t2')
    print()
    print('\t\t|\t\t|')
    print('0\t',board[0][0],'\t|\t',board[0][1],'\t|\t',board[0][2])

    print('    ____________|_______________|_____________')
    print('\t\t|\t\t|')
    print('1\t',board[1][0],'\t|\t',board[1][1],'\t|\t',board[1][2])
    print('    ____________|_______________|_____________')
    print('\t\t|\t\t|')
    print('2\t',board[2][0],'\t|\t',board[2][1],'\t|\t',board[2][2])
    print('\t\t|\t\t|')
    if((board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X' ) or
       (board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X' ) or
       (board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X' ) or
       (board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X' ) or
       (board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X' ) or
       (board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X' ) or
       (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X' ) or
       (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X' )):
        print('!!!Computer Wins!!!')
        time.sleep(4)
        break
    while(1):
        if((board[0][0]=='X' or board[0][0]=='O') and (board[0][1]=='X' or board[0][1]=='O') and (board[0][2]=='X' or board[0][2]=='O') and (board[1][0]=='X' or board[1][0]=='O') and (board[1][1]=='X' or board[1][1]=='O') and (board[1][2]=='X' or board[1][2]=='O') and (board[2][2]=='X' or board[2][2]=='O') and (board[2][1]=='X' or board[2][1]=='O') and (board[2][0]=='X' or board[2][0]=='O')):
            print('\nIts a Tie, Lets try again\n')
            board=[['',' ','  '],['  ',' ',''],['   ','    ','']]
            time.sleep(2)
            os.system('cls')
            print('\t0\t\t1\t\t2')
            print()
            print('\t\t|\t\t|')
            print('0\t',board[0][0],'\t|\t',board[0][1],'\t|\t',board[0][2])

            print('    ____________|_______________|_____________')
            print('\t\t|\t\t|')
            print('1\t',board[1][0],'\t|\t',board[1][1],'\t|\t',board[1][2])
            print('    ____________|_______________|_____________')
            print('\t\t|\t\t|')
            print('2\t',board[2][0],'\t|\t',board[2][1],'\t|\t',board[2][2])
            print('\t\t|\t\t|')
        print('\nYour Turn\n')
        try:
            row=int(input('Enter The Row : '))
            column=int(input('Enter the Column : '))
        except:
            print('Wrong Index Value\nTRY AGAIN')
            continue
            
        if((row <=2 and row >=0 and column <=2 and column>= 0) and board[row][column]!='X' and board[row][column]!='O'):
            board[row][column]='O'
            break
        print('YOU CANNOT INSERT HERE')
        
    

