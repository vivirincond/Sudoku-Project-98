class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen #maybe something else, not so sure yet?

    def set_cell_value(self, value):
        self.value = value