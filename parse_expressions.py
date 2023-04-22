# import json
import pandas as pd
import glob
import MeCab
from preProcessing.preprocessing import preprocessing
# 'D:\M1\fashion\IQON\IQON3000'
filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/77/**/*_new.json")
wakati = MeCab.Tagger("-Owakati")

for fp in filepaths:
    try:
        json_dict = pd.read_json(fp, encoding='shift-jis')
    except Exception as e:
        # print(e)
        # print(fp)
        pass
    for item in json_dict["items"]:
        rm_br_str = preprocessing(item["expressions"][0])
        
        print(rm_br_str)
        # print(wakati.parse(str(rm_br_str)).split())
        