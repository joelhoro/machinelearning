from abc import abstractmethod, ABC

class Game(ABC):
    VERBOSE = True

    def __init__(self):
        self.active_player = 0

    @abstractmethod
    def next_player(self):
        pass

    @abstractmethod
    def get_state(self, move=None):
        pass

    @abstractmethod
    def apply_move(self, move):
        pass

    @abstractmethod
    def is_valid_move(self, move):
        pass

    @abstractmethod
    def finished(self):
        pass

    def submit_move(self, move):
        if self.finished():
            raise Exception("Game is finished")
        if Game.VERBOSE:
            print("Player %s submitting move %s" % (self.active_player, move))
        if not self.is_valid_move(move):
            if Game.VERBOSE:
                print("Invalid move - try again")
                raise Exception("Invalid move")
            return False
        self.apply_move(move)
        self.next_player()
        if Game.VERBOSE:
            print("Applying move, switching to player %s" % self.active_player)
            print("Game state: %s" % self.get_state())
        return True


class TwoPlayerGame(Game):
    def __init__(self):
        super().__init__()

    def get_next_player(self):
        if self.active_player == 0:
            return 1
        return 0

    def next_player(self):
        self.active_player = self.get_next_player()


