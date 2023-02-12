import chess, os

# id -u | 1000
# id -un 1000 | defolt


class GameInfo:
    player1_id = None
    player2_id = None


class GameHandler:
    info = GameInfo()
    board = chess.Board()
    current_turn = 0

    def show(self):
        os.system('cls')
        print(self.board)

    def __init__(self):
        self.show()

    def make_move(self, move):
        if len(move) > 2:
            move.capitalize()
        if self.board.parse_san(move) in self.board.legal_moves:
            self.board.push_san(move)
            self.show()
            print(self.board.legal_moves)
        else:
            print(f"Illegal move {move}")


game = GameHandler()
while 1:
    command = input()
    if command == 'exit':
        break
    game.make_move(command)