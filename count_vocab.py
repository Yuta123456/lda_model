# import json
import pandas as pd
import glob
import MeCab
from preProcessing.preprocessing import preprocessing
wakati = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger()
def parse_sentence(sentence):
    parsed = wakati.parse(sentence).strip().split()
    node = tagger.parseToNode(sentence)
    node = node.next
    result = []
    for w in parsed:
        hinshi = node.feature.split(",")[0]
        result.append((w, hinshi))
        node = node.next
        
    return result

def is_stopword(pos):
    stopwords = ["助詞", "助動詞", "接続詞", "代名詞", "感動詞", "補助記号"]
    return pos in stopwords

import matplotlib.pyplot as plt
def save_word_histogram(word_count_list, filepath):
    words = [word for word, count in word_count_list]
    counts = [count for word, count in word_count_list]

    fig, ax =plt.subplots(figsize=(300, 300))
    ax.bar(words, counts)
    ax.set_xticklabels(words, rotation=90, fontname="Meiryo")
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')

    plt.savefig(filepath)
    plt.close()

# filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/**/**/*_new.json")
fileDir = glob.glob("D:/M1/fashion/IQON/IQON3000/**/")
fileDir = fileDir[:len(fileDir) // 1000]
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
        # print(e)
        continue
    # print(len(json_dict["items"]), fp)
    for item in json_dict["items"]:
        if ("expressions" not in item or len(item["expressions"]) == 0):
            continue
        rm_br_str = preprocessing(item["expressions"][0], debug=False)
        res = parse_sentence(rm_br_str)
        print(res)
        for word, hinshi in res:
            if is_stopword(hinshi):
                continue
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    
    if (c % 100 == 0):
        print(f"{c * 100 / file_count}%終了")
count = sorted(count.items(), key=lambda x: x[1], reverse=True)
count = [t for t in count if t[1] > 200]
save_word_histogram(count, 'frequency.png')


