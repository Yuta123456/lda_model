import numpy as np
import tomotopy as tp

# モデルを読み込む
# D:\M1\fashion\lda_model\lda-T-10-M-5000-R-10-B-1000.bin
mdl = tp.CTModel.load('pa-T-10-M-10000-R-10-B-3000.bin')

# with open('')
# 単語のIDに変換する
def calc_score(fp):
    with open(fp, 'r', encoding="utf-8") as f:
        coordinates = f.read().splitlines()
    ll_sum = 0
    cnt = 0
    coordinates = coordinates[:30000]
    for words in coordinates:
        doc = words.strip().split()
        if len(doc) == 0:
            continue
        inf_doc = mdl.make_doc(doc)
        # print(inf_doc)
        log_prob = mdl.infer(inf_doc, iter=500)[1]
        ll_sum += log_prob
        cnt += 1
        if (cnt % 10000) == 0:
            print(f"{cnt * 100 / len(coordinates)} %終了")
    print(f"{fp}のスコア {ll_sum / len(coordinates)}")

calc_score('data/test_neg.txt')
calc_score('data/test_pos.txt')
calc_score('data/train.txt')