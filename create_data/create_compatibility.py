KEY = "category x color"

# import json
import pandas as pd
import glob


# filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/**/**/*_new.json")
fileDir = glob.glob("D:/M1/fashion/IQON/IQON3000/**/")
filepaths = []
for fd in fileDir:
    filepaths += glob.glob(fd + "**/*_new.json")

count = {}
file_count = len(filepaths)
print(len(filepaths))
c = 0
for fp in filepaths:
    c += 1
    try:
        json_dict = pd.read_json(fp, encoding='shift-jis')
    except Exception as e:
        continue
    for item in json_dict["items"]:
        if (KEY not in item or len(item[KEY]) == 0):
            continue
        category = item[KEY]
        garment = category.split(' × ')[0]
        if garment == "":
            continue
        if garment in count:
            count[garment] += 1
        else:
            count[garment] = 1
    if (c % 100 == 0):
        print(f"{c * 100 / file_count}%終了")
import json
with open('./category.json', 'w', encoding='shift-jis') as f:
    json.dump(count, f, ensure_ascii=False)
count = sorted(count.items(), key=lambda x: x[1], reverse=True)
save_word_histogram(count, 'category.png')


