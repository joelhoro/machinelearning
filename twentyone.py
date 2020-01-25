from game import TwoPlayerGame, Game
import random, math

class TwentyOne(TwoPlayerGame):
    def __init__(self):
        super().__init__()
        self.counter = 21

    def is_valid_move(self, move):
        return move in [1, 2, 3]

    def get_state(self, move=None):
        if move is None:
            move = 0
        return self.counter - move

    def apply_move(self, move):
        self.counter = self.get_state(move)

    def finished(self):
        return self.counter <= 0

    def winner(self):
        return self.get_next_player()


class TwentyOneBot():
    def __init__(self):
        self.stats = [0] * 22
        self.games = 0
        self.moves = []

    def explore(self):
        return random.random() < 0.1

    def initialize(self):
        self.games += 1
        self.moves = []

    def submit_move(self, game, move):
        self.moves.append(game.get_state())
        game.submit_move(move)

    def choose_move(self, game):
        if self.explore():
            return math.floor(random.random() * 3) + 1
        state = game.get_state()
        choices = [1, 2, 3]
        scores = [self.stats[state - choice] for choice in choices]
        # finding the minimal score (for the opponent)
        idx = scores.index(min(scores))
        return idx + 1

    def learn_winner(self, winner):
        for move in self.moves:
            self.stats[move] += winner
            winner = 1 - winner


def play_game(game, bot):
    bot.initialize()
    while not game.finished():
        move = bot.choose_move(game)
        bot.submit_move(game, move)
    bot.learn_winner(game.winner())


if __name__ == "__main__":
    Game.VERBOSE = False

    bot = TwentyOneBot()
    for i in range(100):
        game = TwentyOne()
        play_game(game, bot)

    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('tkagg')
    print(bot.stats)
    plt.bar(range(22), bot.stats)
    plt.show()