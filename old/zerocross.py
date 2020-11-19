print("-"*40)
print("Вас приветствует игра Крестики-Нолики !")
print("-"*40)
print("Перед вами игровое поле!")
print("-"*40)
print("Нужно выбрать номер клетки, куда поставить X для ПЕРВОГО ИГРОКА и O для ВТОРОГО ИГРОКА!")

board = list(range(1,10))
def play_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_input):
    valid = False
    while not valid:
        player_answer = input("Куда поставить"+" "+ player_input+"?")
        player_answer = int(player_answer)
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_input
                valid = True
            else:
                print("Эта клетка занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_winner(board):
    win_numbers = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for number in win_numbers:
        if board[number[0]] == board[number[1]] == board[number[2]]:
            return board[number[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        play_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           if check_winner(board):
              print(check_winner(board), "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    play_board(board)
main(board)
print("Игра окончена!")
print("-" * 13)
input("Нажмите Enter для выхода!")








