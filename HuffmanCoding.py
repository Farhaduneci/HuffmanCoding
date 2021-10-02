from queue import PriorityQueue
import json


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

    def __repr__(self):
        return self.symbol.upper() + str(self.freq)

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


def calcCharFrequencies(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


def calcCodes(node, code='', codes=dict()):
    if(node.left):
        calcCodes(node.left, code + '0', codes)
    if(node.right):
        calcCodes(node.right, code + '1', codes)

    if(not node.left and not node.right):
        codes[node.symbol] = code

    return codes


def encode(data):
    analytics = calcCharFrequencies(data)
    symbols = analytics.keys()

    nodes = PriorityQueue()

    # converting symbols and frequencies into huffman tree nodes
    for symbol in symbols:
        nodes.put(Node(symbol, analytics.get(symbol)))

    while nodes.qsize() > 1:
        # pick 2 smallest nodes
        left, right = nodes.get(), nodes.get()

        # combine the 2 smallest nodes to create new node
        nodes.put(Node(left.symbol + right.symbol,
                       left.freq + right.freq, left, right))

    # extract huffman tree from priority queue
    huffmanTree = nodes.get()

    # calculate encoding code for each character
    codes = calcCodes(huffmanTree)

    print(json.dumps(codes, indent=1))

    encodedData = ''
    for char in data:
        encodedData += codes.get(char)

    # return the encoded output & the huffman tree for future decoding
    return encodedData, huffmanTree


def decode(encodedData, huffmanTree):
    currentNode = huffmanTree
    decodedData = ''

    for bit in encodedData:
        currentNode = currentNode.right if int(bit) == 1 else currentNode.left
        if currentNode.left == None and currentNode.right == None:
            decodedData += currentNode.symbol
            currentNode = huffmanTree

    return decodedData
