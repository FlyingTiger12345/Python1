theboard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '3':' ','2':' ','1':' '}
board_key = []

for key in theboard:
    board_key.append(key)
print(board_key)


def printboards(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printboards(theboard)
        print('its your turn' + turn + "what place?")

        move = input()


        if theboard[move] == ' ':
            theboard[move] = turn
            count +=1
        else:
            print("That place is already filled pick again")
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['7'] == theboard['4'] == theboard['1'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['8'] == theboard['5'] == theboard['2'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['2'] == theboard['4'] == theboard['5'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['9'] == theboard['6'] == theboard['3'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['9'] == theboard['5'] == theboard['1'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] != '':
                printboards(theboard)
                print("gameover")
                print('****' + turn + 'won')
                break
        if count == 9:
            print("game over")
            print("its a tie")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("do u want to restart y/n")
    if restart == "y" or restart == "Y":
        for key in board_key:
            theboard[key] = ''
        game()
if __name__ == "__main__":
    game()