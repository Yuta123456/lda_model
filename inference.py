import numpy as np
import tomotopy as tp

# モデルを読み込む
mdl = tp.LDAModel.load('lda-T-15-M-5000-R-10-B-1000.bin')

# with open('')
# 単語のIDに変換する
def calc_score(fp):
    with open(fp, 'r', encoding="utf-8") as f:
        coordinates = f.read().splitlines()

    ll_sum = 0
    cnt = 0
    for words in coordinates:
        doc = words.strip().split()
        inf_doc = mdl.make_doc(doc)
        log_prob = mdl.infer(inf_doc)[1]
        ll_sum += log_prob
        cnt += 1
        print(f"{cnt * 100 / len(coordinates)} %終了")
    print(f"{fp}のスコア {ll_sum / len(coordinates)}")

calc_score('data/test_neg.txt')
calc_score('data/test_pos.txt')