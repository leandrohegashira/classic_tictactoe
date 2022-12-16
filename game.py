board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}



def printBoard(board):
  print(board['7'] + '|' + board['8'] + '|' + board['9'])
  print('-+-+-')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('-+-+-')
  print(board['1'] + '|' + board['2'] + '|' + board['3'])

      
printBoard(board)


def game():

  turn = 'x'
  count = 0;
    
  for x in board:
    position = input('Wich position do you want to mark: ')

    board[position] == board[x]
    board[position] = turn
    printBoard(board)
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'



    # Check if player wons or it's a tie
    if(board['7'] == board['8'] == board['9'] != ' '):
      printBoard(board)
      print('Player wons') 
      break
    elif(board['4'] == board['5'] == board['6'] != ' '):
      printBoard(board)
      print('Player wons')
      break
    elif(board['1'] == board['2'] == board['3'] != ' '):
      printBoard(board)
      print('Player wons')
      break
    elif(board['1'] == board['4'] == board['7'] != ' '):
      printBoard(board)
      print('Player wons')
      break
    elif(board['2'] == board['5'] == board['8'] != ' '):
      printBoard(board)
      print('Player wons')
      break
    elif(board['3'] == board['6'] == board['9'] != ' '):
      printBoard(board)
      print('Player wons')
    elif(board['1'] == board['5'] == board['6'] != ' '):
      printBoard(board)
      print('Player wons')
      break
    elif(board['3'] == board['5'] == board['7'] != ' '):
      printBoard(board)
      print('Player wons')
      break

  # Repeat game 
  

game()