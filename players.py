from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def learn(self, enemy_move):
        pass


class badGuy(Player):
    def move(self):
        return 0
    
    def learn(self, enemy_move):
        pass

class goodGuy(Player):
    def move(self):
        return 1
    
    def learn(self, enemy_move):
        pass

class TitForTat(Player):
    def __init__(self):
        self.prevMove = 1

    def move(self):
        if(self.prevMove == 1):
            return 1
        else:
            return 0
    
    def learn(self, enemy_move):
        self.prevMove = enemy_move