import sys
import itertools
class TicTacToe:
    def __init__(self):
        self.game = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    ]
        self.col = {
                    'a': 0,
                    'b': 1,
                    'c': 2
                    }
        self.count = 0
        self.moves = []
        self.check = []
        self.left_diag = []
        self.right_diag = []
        print("   a, b, c")
        for count, row in enumerate(self.game):
            print(count, row)

    def user_input(self):
        player_choice = itertools.cycle([1, 2])
        while self.count < 10:
            player = next(player_choice)
            print(f"Current Player: {player}")
            inputs = input("Where do you want to go? eg.a1, b2:   ")
            answer = list(str(inputs))
            if answer not in self.moves:
                self.moves.append(answer)

                self.place_token(answer=answer, player=player)
            else:
                print("This spot is taken, please choose another one!")

    def place_token(self, answer, player):
        if answer[0] in list(self.col.keys()) and int(answer[1]) in list(self.col.values()):
            col_index = self.col[answer[0]]
            row_index = int(answer[1])
            self.game[row_index][col_index] = player

            print("   a, b, c")
            for count, row in enumerate(self.game):
                print(count, row)
            self.count += 1
            print('round',self.count)

            self.win(row_index=row_index, col_index=col_index)

        else:
            print("Please put the right value!")

    def win(self, row_index, col_index):
        # Horizontal
        if self.game[row_index].count(self.game[row_index][0]) == len(self.game[row_index]):
            print("You win!")
            sys.exit()

        # Vertical
        for row in self.game:
            self.check.append(row[col_index])
        if self.check.count(self.check[0]) == len(self.check) and self.check[0] != 0:
            print("You Win!")
            sys.exit()
        else:
            self.check = []

        # Diagonal
        cols = list(reversed(range(len(self.game))))
        for i in range(len(self.game)):
            self.left_diag.append(self.game[i][i])
            self.right_diag.append(self.game[i][cols[i]])
        if self.left_diag.count(self.left_diag[0]) == len(self.left_diag) and self.left_diag[0] != 0:
            print("You Win!")
            sys.exit()
        elif self.right_diag.count(self.right_diag[0]) == len(self.right_diag) and self.right_diag[0] != 0:
            print("You Win!")
            sys.exit()
        else:
            self.left_diag = []
            self.right_diag = []




if __name__ == '__main__':
    game = TicTacToe()
    game.user_input()