import os
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from preProcessing.preprocessing import preprocessing
from util.is_stopword import is_stopword


from util.parse_sentence import parse_sentence


import glob
import pandas as pd

count = {}
with open('data/filepath/test.txt', 'r', encoding="utf-8") as f:
    filepaths = f.read().splitlines()

file_count = len(filepaths)
output_file = "data/test_neg.txt"
c = 0
all_item_captions = []
valid_json_cnt = 0
for fp in filepaths:
    c += 1
    try:
        json_dict = pd.read_json(fp, encoding='shift-jis')
    except Exception as e:
        continue
    valid_json_cnt += 1
    for item in json_dict["items"]:
        if ("expressions" not in item or len(item["expressions"]) == 0):
            continue
        rm_br_str = preprocessing(item["expressions"][0], debug=False)
        res = parse_sentence(rm_br_str)
        words = []
        for word, hinshi in res:
            if is_stopword(hinshi) or len(word) <= 1:
                continue
            words += [word]
        all_item_captions += [words]
        if (c % 100 == 0):
            print(f"{c * 100 / file_count}%終了")

c = 0
random.shuffle(all_item_captions)
# だいたい平均のコーディネートの個数
n = len(all_item_captions) // valid_json_cnt
with open(output_file, mode="w", encoding="utf-8") as f:
    for i in range(len(all_item_captions) // n):
        c += 1
        dummy_coordinates = all_item_captions[n*i:n*(i+1)]
        dummy_coordinates = [w for coordinates in dummy_coordinates for w in coordinates]
        document = " ".join(dummy_coordinates) + '\n'
        f.write(document)
        if (c % 100 == 0):
            print(f"{c * 100 / len(all_item_captions)}%終了")
