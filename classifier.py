# Michael Baart v00199818
# Amy Hanvoravongchai v00822271


import os
import re
import string
import math


def open_files(datafile, labelfile):

    with open(datafile) as f:
        data = f.readlines()
        data = [x.strip() for x in data]

    with open(labelfile) as g:
        labels = g.readlines()
        labels = [x.strip() for x in labels]

    return data,labels

def create_model(data, labels):

    wise_count= 0
    futuristic_count = 0

    data = [x.split() for x in data]
    for i, sentence in enumerate(data):
        for word in sentence:
            if word in model:
                model[word][int(labels[i])] += 1
            else:
                model[word] = [0, 0]
                model[word][int(labels[i])] = 1

        if int(labels[i]) == 0:
            wise_count += 1
        else:
            futuristic_count += 1

    return model, wise_count, futuristic_count


def calc_probability(model, wise_count, futuristic_count, words_array):
    wise_probability = 1
    futuristic_probability = 1

    for word in words_array:

        count = model.get(word)

        if count is None:
            wise_top = 1
            futuristic_top = 1
            
        wise_top = count[0] + 1
        futuristic_top = count[1] + 1



        wise_bot = wise_count + len(model)
        futuristic_bot = futuristic_count + len(model)

        wise_probability *= wise_top / wise_bot
        futuristic_probability *= futuristic_top / futuristic_bot

        print(wise_top)

if __name__ == '__main__':
    model = {}

    traindata_file = "traindata.txt"
    trainlabel_file = "trainlabels.txt"
    train_data, train_labels = open_files(traindata_file, trainlabel_file)
    train_model, train_wise_count, train_futuristic_count = create_model(train_data, train_labels)


    testdata_file = "testdata.txt"
    testlabel_file = "testlabels.txt"
    test_data, test_labels = open_files(testdata_file, testlabel_file)
    test_model, test_wise_count, test_futuristic_count = create_model(test_data, test_labels)

    for i, sentence in enumerate(test_data):
        words_array = sentence.split(' ')
        calc_probability(test_model, test_wise_count, test_futuristic_count, words_array)


    print(train_model)
    print(test_model)


    # print(data)
    # print("\n")
    # print(label)
