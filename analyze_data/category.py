KEY = "category x color"

# import json
import pandas as pd
import glob

import matplotlib.pyplot as plt
def save_word_histogram(word_count_list, filepath):
    words = [word for word, count in word_count_list]
    counts = [count for word, count in word_count_list]

    fig, ax =plt.subplots(figsize=(200, 200))
    ax.bar(words, counts)
    ax.set_xticklabels(words, rotation=90, fontname="Meiryo")
    ax.set_xlabel('category')
    ax.set_ylabel('Frequency')

    plt.savefig(filepath)
    plt.close()

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
count = sorted(count.items(), key=lambda x: x[1], reverse=True)
save_word_histogram(count, 'category.png')


