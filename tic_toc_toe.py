import random
import os

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print('')
        print(' ' + self.board[0][0] + '   |   ' + self.board[0][1] + '   |   ' + self.board[0][2])
        print('--------------------')
        print(' ' + self.board[1][0] + '   |   ' + self.board[1][1] + '   |   ' + self.board[1][2])
        print('--------------------')
        print(' ' + self.board[2][0] + '   |   ' + self.board[2][1] + '   |   ' + self.board[2][2])

    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.done = ''

    def check_win_or_draw(self):
        for i in ['X', 'O']:
            # Horizontais, Verticais e Diagonais
            if (self.board[0][0] == self.board[0][1] == self.board[0][2] == i or
                self.board[1][0] == self.board[1][1] == self.board[1][2] == i or
                self.board[2][0] == self.board[2][1] == self.board[2][2] == i or
                self.board[0][0] == self.board[1][0] == self.board[2][0] == i or
                self.board[0][1] == self.board[1][1] == self.board[2][1] == i or
                self.board[0][2] == self.board[1][2] == self.board[2][2] == i or
                self.board[0][0] == self.board[1][1] == self.board[2][2] == i or
                self.board[2][0] == self.board[1][1] == self.board[0][2] == i):
                self.done = i
                print(i + ' venceu')
                return

        # Empate
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            self.done = 'e'
            print('Empate!')

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                x = int(input('Digite a linha do seu próximo lance: '))
                y = int(input('Digite a coluna do seu próximo lance: '))

                if x < 0 or x > 2 or y < 0 or y > 2:
                    print('Coordenadas inválidas.')
                    continue

                if self.board[x][y] != ' ':
                    print('Posição já preenchida')
                    continue

            except ValueError:
                print('Digite apenas números inteiros.')
                continue

            invalid_move = False
        self.board[x][y] = 'X'

    def make_move(self):
        list_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

        if list_moves:
            x, y = random.choice(list_moves)
            self.board[x][y] = 'O'

tictactoe = TicTacToe()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    tictactoe.print_board()

    while tictactoe.done == '':
        tictactoe.get_player_move()
        tictactoe.check_win_or_draw()
        if tictactoe.done:
            break
        tictactoe.make_move()
        tictactoe.print_board()
        tictactoe.check_win_or_draw()

    play_again = input('Digite 1 para sair do jogo ou tecle qualquer tecla para jogar novamente: ')
    if play_again == '1':
        break
    else:
        tictactoe.reset()

