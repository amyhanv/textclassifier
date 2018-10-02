# Michael Baart v00199818
# Amy Hanvoravongchai v00822271

import os
import re
import string
import math

def get_data(data_file, label_file):

    with open(data_file) as f:
        data = f.readlines()

    with open(label_file) as g:
        labels = g.readlines()

    data = [x.strip() for x in data]
    labels = [x.strip() for x in labels]

    return data, labels

def train_model(data, labels):

    sum_words_wise = 0
    sum_words_prediction = 0
    wise_count = 0
    prediction_count = 0

    data = [x.split() for x in data]
    for i, sentence in enumerate(data):
        for word in sentence:
            if word not in model:
                model[word] = [0, 0]

            model[word][int(labels[i])] += 1

        if int(labels[i]) == 0:
            sum_words_wise += len(sentence)
            wise_count += 1
        else:
            sum_words_prediction += len(sentence)
            prediction_count += 1

    return model, wise_count, prediction_count, sum_words_wise, sum_words_prediction

def calc_cond_probabilities(model, wise_count, pred_count, sum_wise, sum_pred):
    cond_probabilities = {}

    for word in model:
        if word not in cond_probabilities:
            cond_probabilities[word] = [0, 0]

        #calculate conditional probabilities P(word|wise) & P(word|prediction)
        cond_probabilities[word][0] = (model[word][0] + 1)/(sum_wise + len(model))
        cond_probabilities[word][1] = (model[word][1] + 1)/(sum_pred + len(model))

    return cond_probabilities

def classify_test_data(test_data_saying, prob_wise, prob_pred, cond_probs):
    temp_wise = 1
    temp_pred = 1
    for word in test_data_saying:
        if word in model:
            temp_wise *= cond_probs[word][0]
            temp_pred *= cond_probs[word][1]

    temp_wise *= prob_wise
    temp_pred *= prob_pred

    if temp_wise > temp_pred:
        return 0
    return 1

if __name__ == '__main__':
    model = {}

    train_data, train_labels = get_data("traindata.txt", "trainlabels.txt")
    train_model, train_wise_count, train_prediction_count, tot_wise_words, tot_pred_words = train_model(train_data, train_labels)
    
    #P(c) & P(-c)
    probablility_wise = train_wise_count/(train_wise_count + train_prediction_count)
    probablility_prediction = train_prediction_count/(train_wise_count + train_prediction_count)

    #P(Chinese|c),... etc
    conditional_probabilities = {}
    conditional_probabilities = calc_cond_probabilities(train_model, train_wise_count, train_prediction_count, tot_wise_words, tot_pred_words)
    
    # Setup test data
    test_data, test_labels = get_data("testdata.txt", "testlabels.txt")

    result = []
    for i, saying in enumerate(test_data):
        words = saying.split(' ')
        result.append(classify_test_data(words, probablility_wise, probablility_prediction, conditional_probabilities))

    correct = 0
    incorrect = 0
    for i, j in zip(result, test_labels):
        if int(i) == int(j):
            correct += 1
        else:
            incorrect += 1

    print("Accuracy: " + str((correct/len(test_labels))*100))