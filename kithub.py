#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


kit_list = ['あっと', 'えっと', 'おっと', 'かっと', 'がっと', 'きっと', 'Git', 'ぐっと', 'Get', 'God', 'サッと', 'ザッと', 'じっと', 'すっと', 'ずっと', 'Z', 'そっと', 'ぞっと', 'ダッと', '脱兎', 'ちっと', 'どっと', 'ナット', 'ニット', 'ぬっと', 'ネット', 'Net', 'Not', 'はっと', 'バッと', 'パッと', 'Hit', 'びっと', 'ぴっと', 'ふっと', 'ぶっと', 'ぷっと', 'ヘッド', 'べっと', 'ぺっと', 'ほっと', 'ぼっと', 'ぽっと', 'まっと', 'みっと', 'ムッと', 'メット', 'もっと', 'やっと', 'ヨット', 'LiT!', 'レッド', 'ワッと']
hub_list = ['会う', 'あうっ', '悪', '灰汁', '空く', '明日', 'アブ', 'ある', '買う', '書く', '家具', 'カス', '数', '勝つ', 'カツ', 'かぬー', 'カブ', 'かぷっ', '噛む', '粥', '狩る', '額', 'ガス', 'ガブッ', 'ガム', '咲く', '柵', '刺す', '札', '寒', 'サム', 'Sum', '白湯', 'サル', 'ザクッ', '雑', 'ざぶ', 'ザル', '炊く', 'タグ', '足す', '立つ', 'タブ', '樽', 'ダウ', '出す', 'ダブ', 'ダム', 'だる', 'なう', '泣く', 'ナス', '夏', '南無', 'なる', '這う', '吐く', 'ハグ', '蓮', '恥ず', 'ハツ', 'Hub', 'ハブ', '羽生', 'ハム', '春', '貼る', 'バク', 'バグ', 'バス', 'バズ', 'バツ', 'バフ', 'パク', 'パグ', 'パス', 'パフッ', 'パブ', '巻く', 'マグ', 'マス', 'まず', '待つ', '松', 'まぶ', '眉', '丸', 'マル', '焼く', 'やす', 'ヤツ', 'やぶ', 'やる', '楽', 'ラグ', 'ラフ', 'ラブ', 'ラム', '枠', 'わず', '割る']


def main():
    kit = random.choice(kit_list)
    hub = random.choice(hub_list)

    kithub = kit + hub

    print(kithub)


if __name__ == '__main__':
    while True:
        key = input('>>>')
        main()
        if key == 'end':
            break
