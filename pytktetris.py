from __future__ import print_function

import tkinter as tk
import random


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.color = None


class Block:

    BLOCKS = [
        {
            # I block
            'type': 'I',
            'coord': [[1, 1, 1, 1],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#00ffff'
        },
        {
            # J block
            'type': 'J',
            'coord': [[1, 1, 1, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#0000ff'
        },
        {
            # L block
            'type': 'L',
            'coord': [[1, 1, 1, 0],
                      [1, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#ffa500'
        },
        {   # O block
            'type': 'O',
            'coord': [[1, 1, 0, 0],
                      [1, 1, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#ffff00'
        },
        {
            # S block
            'type': 'S',
            'coord': [[0, 1, 1, 0],
                      [1, 1, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#00ff00'
        },
        {
            # T block
            'type': 'T',
            'coord': [[1, 1, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#800080'
        },
        {
            # Z block
            'type': 'Z',
            'coord': [[1, 1, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            'color': '#ff0000'
        }
    ]

    SIZE = 4

    @staticmethod
    def getRandomBlock():
        return random.choice(Block.BLOCKS)

    @staticmethod
    def get_start_column(grid):
        return random.choice(range(grid.length - Block.SIZE))

    @staticmethod
    def get_max_x(block):
        max_x = 0
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                if block['coord'][h][l] == 1:
                    if max_x < l:
                        max_x = l
        return max_x

    @staticmethod
    def get_max_y(block):
        max_y = 0
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                if block['coord'][h][l] == 1:
                    if max_y < h:
                        max_y = h
        return max_y


class Grid:

    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.active_block_x = 0
        self.active_block_y = 0
        self.current_block = None
        self.cells = [[Cell(h, l) for l in range(length)] for h in range(height)]

    def can_move(self, direction):
        if direction == 'space':
            return True
        elif direction == 'left':
            return True
        elif direction == 'right':
            return True
        elif direction == 'down':
            return True
        elif direction == 'up':
            return True
        else:
            # print('Unknown direction to move')
            pass

        return False

    def clear_last_block(self):
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                x = h + self.active_block_x
                y = l + self.active_block_y
                self.cells[x][y].value = 0
                self.cells[x][y].color = None
        # print(self.current_block['coord'])

    def fill_current_block(self):
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                x = self.active_block_x + h
                y = self.active_block_y + l
                self.cells[x][y].value = self.current_block['coord'][h][l]
                self.cells[x][y].color = self.current_block.get('color')

    def move(self, direction):
        if direction == 'space':
            pass

        elif direction == 'left':
            self.clear_last_block()
            self.active_block_y -= 1
            self.fill_current_block()

        elif direction == 'right':
            self.clear_last_block()
            self.active_block_y += 1
            self.fill_current_block()

        elif direction == 'down':
            self.clear_last_block()
            self.active_block_x += 1
            self.fill_current_block()

        elif direction == 'up':
            self.clear_last_block()

            new_block = Block.getRandomBlock()
            while new_block.get('type') == self.current_block.get('type'):
                new_block = Block.getRandomBlock()
            self.current_block = new_block
            self.active_block_x = 0
            start_column = Block.get_start_column(self)
            self.active_block_y = start_column

            self.fill_current_block()

        else:
            # print('Unknown direction to move')
            pass


class GamePanel:

    BG_COLOR = '#ffffff'
    CELL_BG_COLOR = '#ababab'

    SPACE_KEYS = ('space',)
    UP_KEYS = ('w', 'W', 'Up')
    LEFT_KEYS = ('a', 'A', 'Left')
    DOWN_KEYS = ('s', 'S', 'Down')
    RIGHT_KEYS = ('d', 'D', 'Right')

    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.root.title('Tetris')
        self.background = tk.Frame(self.root)
        self.canvas_blocks =[]
        for i in range(self.grid.height):
            canvas_rows = []
            for j in range(self.grid.length):
                canvas = tk.Canvas(self.background, width=32, height=32,
                                   bg=GamePanel.CELL_BG_COLOR)
                canvas.grid(row=i, column=j, padx=1, pady=1)
                canvas_rows.append(canvas)
            self.canvas_blocks.append(canvas_rows)
        self.background.pack()

    def repaint(self):

        for h in range(self.grid.height):
            for l in range(self.grid.length):
                # print('%d\t' % self.grid.cells[h][l].value, end='\t')
                if self.grid.cells[h][l].value == 1:
                    self.canvas_blocks[h][l].configure(bg=self.grid.cells[h][l].color)
                else:
                    self.canvas_blocks[h][l].configure(bg=GamePanel.CELL_BG_COLOR)
            # print('\n')
        # print('game panel repainted')


class Tetris:

    def __init__(self, grid, panel):
        self.grid = grid
        self.panel = panel
        self.game_over = False

    def add_initial_block(self):
        block = Block.getRandomBlock()
        self.grid.current_block = block
        # print('block type: %s' % block['type'] )
        start_column = Block.get_start_column(self.grid)
        self.grid.active_block_y = start_column
        # print('start column: %d' % start_column)

        for i in range(Block.SIZE):
            for j in range(Block.SIZE):
                if block['coord'][i][j] == 1:
                    self.grid.cells[i][j + start_column].value = 1
                    self.grid.cells[i][j + start_column].color = block.get('color')

    def key_handle(self, event):
        if self.game_over:
            return

        pressed_key = event.keysym
        if pressed_key in GamePanel.SPACE_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.can_move('space'):
                self.grid.move('space')

        elif pressed_key in GamePanel.LEFT_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.can_move('left'):
                self.grid.move('left')

        elif pressed_key in GamePanel.RIGHT_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.can_move('right'):
                self.grid.move('right')

        elif pressed_key in GamePanel.DOWN_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.can_move('down'):
                self.grid.move('down')

        elif pressed_key in GamePanel.UP_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.can_move('up'):
                self.grid.move('up')
        else:
            pass

        self.panel.repaint()

    def start(self):
        self.add_initial_block()
        self.panel.repaint()
        self.panel.root.bind('<Key>', self.key_handle)
        self.panel.root.mainloop()


if __name__ == '__main__':
    grid = Grid(10, 20)
    panel = GamePanel(grid)
    tetris = Tetris(grid, panel)
    tetris.start()
