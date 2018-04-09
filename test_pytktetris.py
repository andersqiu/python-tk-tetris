import unittest
import pytktetris

class TestBlock(unittest.TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_block(self):
        i_block = pytktetris.Block.BLOCKS[0]
        self.assertEqual(pytktetris.Block.get_max_x(i_block), 3)
        self.assertEqual(pytktetris.Block.get_max_y(i_block), 0)

        o_block = pytktetris.Block.BLOCKS[3]
        self.assertEqual(pytktetris.Block.get_max_x(o_block), 1)
        self.assertEqual(pytktetris.Block.get_max_y(o_block), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)