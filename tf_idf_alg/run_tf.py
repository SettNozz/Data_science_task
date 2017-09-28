import collections
import re
import math


def compute_tf_idf(text_s):
        def compute_tf(text):
            tf_text = collections.Counter(text)
            for word in tf_text:
                tf_text[word] = tf_text[word]/float(len(tf_text))
            return tf_text

        def compute_idf(word, text_s):
            return math.log10(len(text_s) / sum([1.0 for i in text_s if word in i]))

        doc_list = []
        for text in text_s:
            tf_idf_dict = {}
            computed_tf = compute_tf(text)
            for words in computed_tf:
                tf_idf_dict[words] = computed_tf[words] * compute_idf(words, text_s)
                doc_list.append(tf_idf_dict)
        return doc_list


def file_to_list(filename):
    text_1 = []
    with open(filename, 'r') as file:
        data = file.read()
        text_ = re.split('[^a-z]', data.lower())
        for i in text_:
            if i != '':
                text_1.append(i)
        #print text_1
    file.close()
    return text_1

file_1 = 'text1.txt'
file_2 = 'text2.txt'


text1 = file_to_list(file_1)
text2 = file_to_list(file_2)
texts = [text1, text2]

print compute_tf_idf(texts)