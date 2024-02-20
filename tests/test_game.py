# tests/test_game.py
from longest_word.game import Game
import string
class TestGame:
    def test_game_initialization(self):

            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_game_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'OQUWRBAZE'

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert not new_game.is_valid('PROUT')
        assert new_game.is_valid('BAROQUE')

        # teardown
        assert new_game.grid == list(test_grid)
