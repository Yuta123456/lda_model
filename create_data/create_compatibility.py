KEY = "category x color"

# import json
import pandas as pd
import glob

def is_tops(g):
    return g in ["ジャケット", "トップス", "コート", "ニット", "タンクトップ", "ブラウス", "Tシャツ", "カーディガン", "ダウンジャケット", "パーカー"]

def is_bottoms(g):
    return g in ['スカート', 'ロングスカート', "ロングパンツ"]

def is_shoes(g):
    return g in ["ブーツ", "パンプス", "スニーカー", "靴", "サンダル"]

def add_count(d, i1, i2, i3, w):
    if i1 not in d:
        d[i1] = {}
    if i2 not in d[i1]:
        d[i1][i2] = {}
    if i3 not in d[i1][i2]:
        d[i1][i2][i3] = 0
    d[i1][i2][i3] += w
# filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/**/**/*_new.json")
fileDir = glob.glob("D:/M1/fashion/IQON/IQON3000/**/")
filepaths = []
for fd in fileDir:
    filepaths += glob.glob(fd + "**/*_new.json")
tops_count = {}
bottoms_count = {}
shoes_count = {}

file_count = len(filepaths)
print(len(filepaths))
for c, fp in enumerate(filepaths):
    try:
        coordinate = pd.read_json(fp, encoding='shift-jis')
    except Exception as e:
        continue
    # 各コーディネートの情報が手に入る
    # 一応、like_countもある。
    weight = coordinate["likeCount"]
    weight = 1 if len(weight) == 0 else int(weight[0])
    tops = []
    bottoms = []
    shoes = []
    for item in coordinate["items"]:
        if (KEY not in item or len(item[KEY]) == 0):
            continue
        category = item[KEY]
        garment = category.split(' × ')[0]
        if is_tops(garment):
            tops.append(category)
        if is_bottoms(garment):
            bottoms.append(category)
        if is_shoes(garment):
            shoes.append(category)
    for t in tops:
        for b in bottoms:
            for s in shoes:
                add_count(tops_count, b, s, t, weight)
                add_count(bottoms_count, t, s, b, weight)
                add_count(shoes_count, t, b, s, weight)
    if (c % 100 == 0):
        p = (c * 100 // file_count)
        progress = '=' * p + ' ' * (100-p)
        print(f"\r【{progress}】{p}%", end='')

import json
with open('./tops_count.json', 'w', encoding='shift-jis') as f:
    json.dump(tops_count, f, ensure_ascii=False)

with open('./bottoms_count.json', 'w', encoding='shift-jis') as f:
    json.dump(bottoms_count, f, ensure_ascii=False)

with open('./shoes_count.json', 'w', encoding='shift-jis') as f:
    json.dump(shoes_count, f, ensure_ascii=False)

