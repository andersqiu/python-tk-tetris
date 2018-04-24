from __future__ import print_function

import tkinter as tk
import random
import threading


class Cell:

    def __init__(self, h, l):
        self.h = h
        self.l = l
        self.value = 0
        self.color = None


class Block:

    BLOCKS = [
        {
            # I block
            'type': 'I',
            'coord': [[
                        [1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]
                      ],
                      [
                        [1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]
                      ]
                     ],
            'color': '#00ffff'
        },
        {
            # J block
            'type': 'J',
            'coord': [[
                        [1, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#0000ff'
        },
        {
            # L block
            'type': 'L',
            'coord': [[
                        [1, 1, 1, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 0, 1, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#ffa500'
        },
        {   # O block
            'type': 'O',
            'coord': [[
                        [1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#ffff00'
        },
        {
            # S block
            'type': 'S',
            'coord': [[
                        [0, 1, 1, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 1, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#00ff00'
        },
        {
            # T block
            'type': 'T',
            'coord': [[
                        [1, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#800080'
        },
        {
            # Z block
            'type': 'Z',
            'coord': [[
                        [1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                      ],
                      [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0]
                      ]
                     ],
            'color': '#ff0000'
        }
    ]

    SIZE = 4

    @staticmethod
    def pick_block():
        return random.choice(Block.BLOCKS)

    @staticmethod
    def get_start_column(grid):
        return random.choice(range(grid.length - Block.SIZE))


class Grid:

    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.active_block_row = 0
        self.active_block_col = 0
        self.current_block = None
        self.current_block_form = 0
        self.cells = [[Cell(h, l) for l in range(length)] for h in range(height)]

    def can_add_block(self):
        return True

    def block_can_rotate(self):
        return True

    def has_full_row(self):
        found_full_rows = []
        for h in range(self.height):
            full_row = True
            for l in range(self.length):
                if self.cells[h][l].value == 0:
                    full_row = False
                    break
            found_full_rows.append(full_row)
        return any(found_full_rows)

    def is_full_row(self, h):
        if h < 0 or h >= self.height:
            return False

        for l in range(self.length):
            if self.cells[h][l].value == 0:
                return False
        return True

    def add_new_block(self):
        self.active_block_row = 0
        self.active_block_col = Block.get_start_column(self)

        block = Block.pick_block()
        self.current_block = block
        self.current_block_form = 0

        if self.can_add_block():
            self.fill_current_block()

    def can_move(self, direction):
        if direction == 'space':
            return True

        elif direction == 'left':
            rows_can_move = []
            for h in range(Block.SIZE):
                if not any(self.current_block['coord'][self.current_block_form][h]):
                    continue

                l = 0
                while self.current_block['coord'][self.current_block_form][h][l] == 0 \
                        and l < Block.SIZE:
                    l += 1
                row = self.active_block_row + h
                col = self.active_block_col + l - 1
                if col < 0 or row >= self.height:
                    return False
                else:
                    if self.cells[row][col].value == 1:
                        rows_can_move.append(False)
                    else:
                        rows_can_move.append(True)

            return all(rows_can_move)

        elif direction == 'right':
            rows_can_move = []
            for h in range(Block.SIZE):
                if not any(self.current_block['coord'][self.current_block_form][h]):
                    continue

                l = Block.SIZE - 1
                while self.current_block['coord'][self.current_block_form][h][l] == 0 \
                        and l >= 0:
                    l -= 1
                row = self.active_block_row + h
                col = self.active_block_col + l + 1
                if col >= self.length or row >= self.height:
                    return False
                else:
                    if self.cells[row][col].value == 1:
                        rows_can_move.append(False)
                    else:
                        rows_can_move.append(True)

            return all(rows_can_move)

        elif direction == 'down':
            form = self.current_block_form
            cols_can_move = []
            for l in range(Block.SIZE):
                col = []
                for h in range(Block.SIZE):
                    col.append(self.current_block['coord'][form][h][l])
                if not any(col):
                    continue

                h = Block.SIZE - 1
                while col[h] == 0 and h >= 0:
                    h -= 1
                row = self.active_block_row + h + 1
                col = self.active_block_col + l
                if row >= self.height or col >= self.length:
                    return False
                else:
                    if self.cells[row][col].value == 1:
                        cols_can_move.append(False)
                    else:
                        cols_can_move.append(True)

            return all(cols_can_move)

        # elif direction == 'up':
        #     new_form = (self.current_block_form + 1) % Block.SIZE
        #     for h in range(Block.SIZE):
        #         for l in range(Block.SIZE):
        #             if self.current_block['coord'][new_form][h][l] == 1:
        #                 row = self.active_block_row + h
        #                 col = self.active_block_col + l
        #                 if self.cells[row][col].value == 1:
        #                     return False
        #     return True
        else:
            # print('Unknown direction to move')
            pass

        return False

    def clear_last_block(self):
        form = self.current_block_form
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                row = self.active_block_row + h
                col = self.active_block_col + l
                if 0 <= row < self.height and 0 <= col < self.length:
                    if self.current_block['coord'][form][h][l] == 1:
                        self.cells[row][col].value = 0
                        self.cells[row][col].color = None

    def fill_current_block(self):
        form = self.current_block_form
        for h in range(Block.SIZE):
            for l in range(Block.SIZE):
                row = self.active_block_row + h
                col = self.active_block_col + l

                if 0 <= row < self.height and 0 <= col < self.length:
                    if self.current_block['coord'][form][h][l] == 1:
                        self.cells[row][col].value = self.current_block['coord'][form][h][l]
                        self.cells[row][col].color = self.current_block.get('color')

    def move(self, direction):
        if direction == 'left':
            self.clear_last_block()
            self.active_block_col -= 1
            self.fill_current_block()

        elif direction == 'right':
            self.clear_last_block()
            self.active_block_col += 1
            self.fill_current_block()

        elif direction == 'down':
            self.clear_last_block()
            self.active_block_row += 1
            self.fill_current_block()

        # elif direction == 'up':
        #
        #     self.clear_last_block()
        #     self.current_block_form += 1
        #     self.current_block_form %= Block.SIZE
        #     print(self.current_block_form)
        #     self.fill_current_block()

        else:
            # print('Unknown direction to move')
            pass

    def rotate_block(self):
        self.clear_last_block()
        self.current_block_form += 1
        self.current_block_form %= Block.SIZE
        # print(self.current_block_form)
        self.fill_current_block()

    def remove_full_rows(self):
        new_cells = [[Cell(h, l) for l in range(self.length)]
                                 for h in range(self.height)]
        new_row = self.height - 1
        full_rows_num = 0
        for h in range(self.height - 1, -1, -1):
            if self.is_full_row(h):
                full_rows_num += 1
                continue
            for l in range(self.length):
                new_cells[new_row][l].value = self.cells[h][l].value
                new_cells[new_row][l].color = self.cells[h][l].color
            new_row -= 1

        for h in range(self.height):
            for l in range(self.length):
                self.cells[h][l].value = new_cells[h][l].value
                self.cells[h][l].color = new_cells[h][l].color

        # Todo:
        # There're bugs here
        self.clear_last_block()
        self.active_block_col += full_rows_num
        self.fill_current_block()


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

        # print('%d， %d' % (self.grid.active_block_x, self.grid.active_block_y))
        for h in range(self.grid.height):
            for l in range(self.grid.length):
                # print('%d\t' % self.grid.cells[h][l].value, end='\t')
                if self.grid.cells[h][l].value == 1:
                    self.canvas_blocks[h][l].configure(bg=self.grid.cells[h][l].color)
                else:
                    self.canvas_blocks[h][l].configure(bg=GamePanel.CELL_BG_COLOR)
            # print('\n')


class Tetris:

    def __init__(self, grid, panel):
        self.grid = grid
        self.panel = panel
        self.game_over = False

        self.lock = threading.Lock()

    def key_handle(self, event):
        if self.game_over:
            return

        pressed_key = event.keysym
        if pressed_key in GamePanel.SPACE_KEYS:
            # print('%s key pressed' % pressed_key)

            while self.grid.can_move('down'):
                self.grid.move('down')
            self.grid.add_new_block()

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

            if not self.grid.can_move('down'):
                self.grid.add_new_block()

        elif pressed_key in GamePanel.UP_KEYS:
            # print('%s key pressed' % pressed_key)

            if self.grid.block_can_rotate():
                self.grid.rotate_block()
        else:
            pass

        # print(self.grid.has_full_row())
        if self.grid.has_full_row():
            self.grid.remove_full_rows()
        self.panel.repaint()

    def start(self):
        self.grid.add_new_block()
        self.panel.repaint()
        self.panel.root.bind('<Key>', self.key_handle)
        self.panel.root.mainloop()


if __name__ == '__main__':
    grid = Grid(10, 20)
    panel = GamePanel(grid)
    tetris = Tetris(grid, panel)
    tetris.start()
