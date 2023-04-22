# import json
import pandas as pd
import glob
import MeCab
from preProcessing.preprocessing import preprocessing
# 'D:\M1\fashion\IQON\IQON3000'
# 。3966621\3966621_new.json

filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/1468/**/*_new.json")
# filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/1468/3966621/3966621_new.json")
wakati = MeCab.Tagger("-Owakati")
for fp in filepaths:
    try:
        json_dict = pd.read_json(fp, encoding='shift-jis')
    except Exception as e:
        # print(e)
        continue
    # print(len(json_dict["items"]), fp)
    for item in json_dict["items"]:
        rm_br_str = preprocessing(item["expressions"][0], debug=False)
        print(rm_br_str)
        # if (rm_br_str == ""):
        #     print(fp)
        #     print("="*100, "\n", item["expressions"][0], "\n","="*100)
        # else:
            
        # print(wakati.parse(str(rm_br_str)).split())
        