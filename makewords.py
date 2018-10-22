#!/usr/bin/env python
# -*- coding: utf-8 -*-

from natto import MeCab
import kakasi_helper as kh


hiragana = [chr(i) for i in range(12353, 12436)]


def get_two_letter_words():
    two_letter_words = []

    for first in hiragana:
        if first not in 'ぁぃぅぇぉゃゅょゎん':
            for last in hiragana:
                two_letter_words.append(first + last)

    return two_letter_words


def write_to_file():
    with open('./au.txt', mode='w') as f:
        f.writelines('\n'.join(find_au_words()))


def read_from_file():
    au_list = []
    with open('./au.txt', mode='r') as f:
        for line in f:
            au_list.append(line[:-1])

    return au_list


def tokenize(text):
    tokens = []
    with MeCab('-F%f[0],%f[6]') as nm:
        for n in nm.parse(text, as_nodes=True):
            # ignore any end-of-sentence nodes
            if not n.is_eos() and n.is_nor():
                klass, word = n.feature.split(',', 1)
                if klass in ['名詞', '形容詞', '形容動詞', '動詞', '副詞']:
                    tokens.append(word)
    return tokens


def tokenize_all(text):
    with MeCab('-F%f[0],%f[6]') as nm:
        print(text + ': ' + nm.parse(text))


def find_au_words():
    tlw = get_two_letter_words()
    au_words = []

    for word in tlw:
        vowels = kh.get_vowels(word)
        if vowels == 'au':
            au_words.append(word)

    return au_words


def find_valid_words():
    au_words = find_au_words()
    words = []
    for word in au_words:
        # words = tokenize(word)
        tokenize_all(word)

    print(words)


def get_tto_words():
    tto_words = []
    for first in hiragana:
        if first not in 'ぁぃぅぇぉゃゅょゎん':
            tto_words.append(first + 'っと')
    return tto_words


if __name__ == '__main__':
    print(get_tto_words())
