class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        # symbol
        self.symbol = symbol

        # frequency of symbol
        self.freq = freq

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''
