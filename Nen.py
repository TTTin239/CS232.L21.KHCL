# import cv2 as cv
# import numpy as np

# ##Color image grayscale
# image = cv.imread('Dep.bmp',1)
# grayimg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow('grayimg',grayimg)
# cv.waitKey(3000)
# rows, cols = grayimg.shape

# image1 = grayimg.flatten() #Reduce the dimensionality of the grayscaled two-dimensional image to a one-dimensional list
# print(len(image1))

# #Binarization operation
# for i in range(len(image1)):
#     if image1[i] >= 127:
#         image1[i] = 255
#     if image1[i] < 127:
#         image1[i] = 0

# print(image1)
# image2 = image1.reshape(rows,cols)
# cv.imshow('image2',image2)
# cv.waitKey(3000)

# data = []
# image3 = []
# count = 1
# #Stroke compression encoding
# for i in range(len(image1)-1):
#     if (count == 1):
#         image3.append(image1[i])
#     if image1[i] == image1[i+1]:
#         count = count + 1
#         if i == len(image1) - 2:
#             image3.append(image1[i])
#             data.append(count)
#     else:
#         data.append(count)
#         count = 1

# if(image1[len(image1)-1] != image1[-1]):
#     image3.append(image1[len(image1)-1])
#     data.append(1)

# # print(data)
# print(data)
# #print(image3)


# #Compression ratio
# ys_rate = len(image3)/len(image1)*100
# print(str(ys_rate) + '%')

# #Stroke encoding and decoding
# rec_image = []
# for i in range(len(data)):
#     for j in range(data[i]):
#         rec_image.append(image3[i])

# rec_image = np.reshape(rec_image,(rows,cols))
# print(rec_image)

# cv.imshow('rec_image',rec_image) #Re-output the binarized image
# cv.waitKey(0)

import math
import sys
global probabilities
probabilities = []

class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1

    def characteristics_huffman_code(self, code):
        length_of_code = [len(k) for k in code]

        mean_length = sum([a*b for a, b in zip(length_of_code, self.probability)])
        
        entropy_of_code= sum(length_of_code)*4
                
        print("Average length of the code: %f" % mean_length)
        print("Efficiency of the code: %f" % (entropy_of_code/mean_length))

    def compute_code(self):
        num = len(self.probability)
        huffman_code = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman_code[num-i-1] != '' and huffman_code[num-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[num-i-1] != ''):
                huffman_code[num-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[num-i-2] != ''):
                huffman_code[num-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num-i-1] = '1'
                huffman_code[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[num-i-2], list) and isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + huffman_code[num-i-2]
            elif(isinstance(huffman_code[num-i-2], list)):
                complete_code = huffman_code[num-i-2] + [huffman_code[num-i-1]]
            elif(isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + [huffman_code[num-i-2]]
            else:
                complete_code = [huffman_code[num-i-2], huffman_code[num-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

string = input("Enter the string to compute Huffman Code: ")

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True)

huffmanClassObject = HuffmanCode(probabilities)
P = probabilities

huffman_code = huffmanClassObject.compute_code()

print(' Char | Huffman code ')
print('----------------------')

for id,char in enumerate(freq):
    if huffman_code[id]=='':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_code[id]))

huffmanClassObject.characteristics_huffman_code(huffman_code)

# # Huffman Coding in python

# string = 'BCAADDDCCACACAC'


# # Creating tree nodes
# class NodeTree(object):

#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right

#     def children(self):
#         return (self.left, self.right)

#     def nodes(self):
#         return (self.left, self.right)

#     def __str__(self):
#         return '%s_%s' % (self.left, self.right)


# # Main function implementing huffman coding
# def huffman_code_tree(node, left=True, binString=''):
#     if type(node) is str:
#         return {node: binString}
#     (l, r) = node.children()
#     d = dict()
#     d.update(huffman_code_tree(l, True, binString + '0'))
#     d.update(huffman_code_tree(r, False, binString + '1'))
#     return d


# # Calculating frequency
# freq = {}
# for c in string:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1

# freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# nodes = freq

# while len(nodes) > 1:
#     (key1, c1) = nodes[-1]
#     (key2, c2) = nodes[-2]
#     nodes = nodes[:-2]
#     node = NodeTree(key1, key2)
#     nodes.append((node, c1 + c2))

#     nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

# huffmanCode = huffman_code_tree(nodes[0][0])

# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))