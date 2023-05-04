def is_stopword(pos):
    stopwords = ["助詞", "助動詞", "接続詞", "代名詞", "感動詞", "補助記号"]
    return pos in stopwords