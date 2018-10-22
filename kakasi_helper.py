#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()


# 単語をローマ字に変換する
def convert_to_roman(word):
    return conv.do(word)


# 単語から母音を抽出する
def get_vowels(word):
    vowels = ''
    roman_word = convert_to_roman(word)

    for i, letter in enumerate(roman_word):
        if letter in 'aiueo':
            vowels += letter
        # elif letter is roman_word[i+1]:
        #     vowels += letter
    return vowels
