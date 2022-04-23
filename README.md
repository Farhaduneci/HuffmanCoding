# Huffman Coding Compression Algorithm

Huffman Coding Algorithm implemented in Python

## Demo
```bash
python3 HuffmanCoding.py -d "Hello World"
```
```bash
{
 " ": "000",
 "d": "001",
 "H": "010",
 "W": "011",
 "l": "10",
 "o": "110",
 "r": "1110",
 "e": "1111"
}

Encoded: 01011111010110000011110111010001

ASCII: 77 bit, HUFFMAN: 32 bit.

Decoded: Hello World
```

## Resources
- https://en.wikipedia.org/wiki/Huffman_coding
- https://www.programiz.com/dsa/huffman-coding
- https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
