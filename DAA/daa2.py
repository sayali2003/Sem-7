#Implement job sequencing with deadlines using a greedy method.

import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=''

    def __lt__(self, nxt):
        return self.freq < nxt.freq
    
def print_nodes(node, val=''):
    new_val= val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

def huffman_encoding_menu():
    chars=[]
    freq=[]
    n=int(input("enter no. of characters: "))
    for i in range(n):
        c=input("enter character: ")
        f=int(input("enter its frequency: "))
        chars.append(c)
        freq.append(f)
    print(chars)
    print(freq)
    nodes=[]

    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    while len(nodes) > 1:
        left= heapq.heappop(nodes)
        right=heapq.heappop(nodes)
        left.huff=0
        right.huff=1
        new_node=Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("Huffman codes: ")
    print_nodes(nodes[0])

if __name__=="__main__":
    huffman_encoding_menu()
