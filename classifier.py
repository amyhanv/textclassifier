import os
import re
import string
import math


def open_files(datafile, labelfile):

    with open(datafile) as f:
        data = f.readlines()
        data = [x.strip() for x in data]

    with open(labelfile) as g:
        label = g.readlines()
        label = [x.strip() for x in label]

    return data, label

if __name__ == '__main__':
    traindata = "traindata.txt"
    trainlabel = "trainlabels.txt"
    testdata = "testdata.txt"
    testlabel = "testlabels.txt"

    data_and_label = open_files(traindata, trainlabel)
    print (data_and_label[0])
