import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from preProcessing.preprocessing import preprocessing
from util.is_stopword import is_stopword


from util.parse_sentence import parse_sentence


import glob
import pandas as pd
KEY = "category x color"
count = {}
with open('data/filepath/test.txt', 'r', encoding="utf-8") as f:
    filepaths = f.read().splitlines()

file_count = len(filepaths)
output_file = "data/test_pos.txt"
c = 0
with open(output_file, mode="a", encoding="utf-8") as f:
    for fp in filepaths:
        c += 1
        try:
            json_dict = pd.read_json(fp, encoding='shift-jis')
        except Exception as e:
            continue
        # documentを格納
        words = []
        for item in json_dict["items"]:
            if ("expressions" not in item or len(item["expressions"]) == 0):
                continue
            rm_br_str = preprocessing(item["expressions"][0], debug=False)
            res = parse_sentence(rm_br_str)
            category = item[KEY].split(' × ')[0]
            for word, hinshi in res:
                if is_stopword(hinshi) or len(word) <= 1:
                    continue
                words += [category + '_' + word]
        document = " ".join(words) + "\n"

        f.write(document)
        if (c % 100 == 0):
            print(f"{c * 100 / file_count}%終了")
