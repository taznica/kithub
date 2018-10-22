#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def get_list_from_csv():
    with open('./keywordlist_furigana.csv', 'r') as f:
        content = csv.DictReader(f, delimiter=',', lineterminator='\r\n', skipinitialspace=True)
        header = next(content)

        for row in content:
            print(row)


if __name__ == '__main__':
    get_list_from_csv()
