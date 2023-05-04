import numpy as np
import tomotopy as tp

# モデルを読み込む
mdl = tp.LDAModel.load('model.bin')

# with open('')
# 単語のIDに変換する
word_ids = [mdl.vocabulary.get(term, -1) for term in words]

# モデルから推定する
doc = tp.utils.BagOfWords(word_ids)
log_prob = mdl.infer(doc)[0]

# 対数尤度を確率に変換する
prob = np.exp(log_prob)

print(f"文章の生成確率: {prob}")
