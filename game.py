board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}



def printBoard(board):
  print(board['7'] + '|' + board['8'] + '|' + board['9'])
  print('-+-+-')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('-+-+-')
  print(board['1'] + '|' + board['2'] + '|' + board['3'])


def playAgain():
  repeat = input('Do you want to play again y/n? ')

  while repeat == 'y':
    for key in board:
      board[key] = ' '
    game()
    playAgain()
  quit()  


printBoard(board)


def game():

  turn = 'x'
  count = 1
    
  for x in board:

    while count < 10:

      position = input('Wich position do you want to mark: ')
      board[position] == board[x]
      board[position] = turn
      printBoard(board)
      count+=1

      # Check wich player won
      if(board['7'] == board['8'] == board['9'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won') 
        break
      elif(board['4'] == board['5'] == board['6'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break
      elif(board['1'] == board['2'] == board['3'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break
      elif(board['1'] == board['4'] == board['7'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won') 
        break
      elif(board['2'] == board['5'] == board['8'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break
      elif(board['3'] == board['6'] == board['9'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break
      elif(board['1'] == board['5'] == board['6'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break
      elif(board['3'] == board['5'] == board['7'] != ' '):
        printBoard(board)
        print(f'Player "{turn}" won')
        break

      # Swich the turn of players
      if turn == 'x':
        turn = 'o'
      else:
        turn = 'x'

    break

game()
playAgain()