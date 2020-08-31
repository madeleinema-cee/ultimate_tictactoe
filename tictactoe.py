

class TicTacToe:
    def __init__(self):
        self.game = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],]
        self.col = {
                    'a': 0,
                    'b': 1,
                    'c': 2
                    }

        self.count = 1
        print("   a, b, c")
        for count, row in enumerate(self.game):
            print(count, row)

    def user_input(self):

        while self.count < 10:
            answer = list(str(input("Where do you want to go? eg.a1, b2:   ")))
            self.place_token(answer=answer)



    def place_token(self, answer):
        if answer[0] in list(self.col.keys()) and int(answer[1]) in list(self.col.values()):
            col_index = self.col[answer[0]]
            row_index = int(answer[1])
            self.game[row_index][col_index] = 1

            print("   a, b, c")
            for count, row in enumerate(self.game):
                print(count, row)
            self.count += 1
            print(self.count)
        else:
            print("Please put the right value!")



if __name__ == '__main__':
    game = TicTacToe()
    game.user_input()