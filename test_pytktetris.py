import unittest
import pytktetris

class TestBlock(unittest.TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_can_move1(self):
        grid = pytktetris.Grid(10, 20)
        grid.active_block_row = 0
        grid.active_block_col = 7
        grid.current_block = pytktetris.Block.BLOCKS[-2]

        self.assertFalse(grid.can_move('right'))


if __name__ == '__main__':
    unittest.main(verbosity=2)