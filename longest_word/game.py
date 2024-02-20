import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        if word is None:
            return False
        word_list = list(word)
        for word in word_list:
            if not word in self.grid:
                return False
        return True
