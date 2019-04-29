# -*- coding:utf-8 -*-
__author__ = 'LiLei'

class Node(object):
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
    def isLeft(self):
        return self.father.left == self

def createNodes(freqs):
    return [Node(freq) for freq in freqs]

def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

'''
nodes: the all nodes made up the huffman tree
root: the huffman tree
'''
def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

'''
if __name__ == '__main__':
    key_list = ['1','2','3','4']
    nodes = createNodes([100,20,50,1])
    root = createHuffmanTree(nodes)
    codec = huffmanEncoding(nodes,root)
    print(codec)
    dict_ = dict(zip(key_list,codec))
    print(dict_)
'''

