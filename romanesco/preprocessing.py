#!/usr/bin/python3
#-*- coding: utf-8 -*-


from nltk import sent_tokenize
from nltk import word_tokenize
from random import shuffle
import sys


def rmv_newlines(filename):
    filename += ".txt"
    with open(filename, "r", encoding="utf-8") as infile:
        infile = infile.read()
        text = str()
        for line in infile:
            text += line.strip("\n")
    return text


def tokenize(text):
    sents = sent_tokenize(text)
    words = list()
    for sent in sents:
        words.append(word_tokenize(sent))
    return words


def normalize_case(text, how="lower"):
    def normalize(input):
        if how == "lower":
            return input.lower()
        elif how == "upper":
            return input.upper()
    for i in range (0, len(text)):
        for j in range (0, len(text[i])):
            text[i][j] = normalize(text[i][j])
    return text


def split_corpus_into_sets(sentences, filename):
    shuffle(sentences)
    dev_n = round(len(sentences) / 10)
    dev_name = filename + ".dev"
    train_name = filename + ".train"
    with open(dev_name, "w+", encoding="utf-8") as dev, \
        open (train_name, "w+", encoding="utf-8") as train:
        for sent in sentences[:dev_n]:
            for word in sent:
                dev.write(word)
                dev.write(" ")
            dev.write("\n")
        for sent in sentences[dev_n:]:
            for word in sent:
                train.write(word)
                train.write(" ")
            train.write("\n")


def main(filename):
    raw_text = rmv_newlines(filename)
    tokenized_text = tokenize(raw_text)
    lowercased_text = normalize_case(tokenized_text, "lower")
    split_corpus_into_sets(lowercased_text, filename)


if __name__ == "__main__":
    main("goethe")
