# import json
import pandas as pd
import glob
import MeCab
from preProcessing.preprocessing import preprocessing
# 'D:\M1\fashion\IQON\IQON3000'
filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/77/3907846/*_new.json")
wakati = MeCab.Tagger("-Owakati")
print(filepaths)
for fp in filepaths:
    json_dict = pd.read_json(fp, encoding='shift-jis')
    for item in json_dict["items"]:
        rm_br_str = preprocessing(item["expressions"][0])
        
        print(rm_br_str)
        # print(wakati.parse(str(rm_br_str)).split())
        