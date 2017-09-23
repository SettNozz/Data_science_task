import re
import numpy as np
import scipy.spatial


with open('sentences.txt', 'r') as file:
    data_file = file.readlines()

i=0
for sent in data_file:
    sent = re.split('[^a-z]', sent.lower())
    data_file[i] = filter(None, sent)
    i+=1

word_index = dict()
i = 0
for sentence in data_file:
    for word in sentence:
        if word not in word_index:
            word_index[word] = i
            i += 1

matrix = []
for sent_i in xrange(0, len(data_file)):
    matrix.append([0 for x in word_index])

    for word in data_file[sent_i]:
        word_i = word_index[word]
        matrix[sent_i][word_i] += 1

np_matrix = np.array(matrix)

distances = list()
for i in range(len(data_file)):
    distance = scipy.spatial.distance.cosine(np_matrix[0], np_matrix[i])
    distances.append((i, distance))

sorted_list = sorted(distances, key=lambda tup: tup[1])

print sorted_list[1][0], sorted_list[2][0]
