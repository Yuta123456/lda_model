def preprocessing(line, debug=False):
    preprocesser = [remove_item_description,
                     remove_sentences_with_word, remove_after_item_number,
                     remove_after_model_info, remove_extra_info]
    # 最後に追加
    preprocesser.append(remove_newlines)
    for p in preprocesser:
        line = p(line)
        if debug:
            print(f"{p.__name__}",line)
    return line

def remove_item_description(line):
    # アイテム説明のインデックスを検索
    index = line.find("アイテム説明")
    if index != -1:
        # アイテム説明の前のテキストとアイテム説明以降のテキストを連結する
        line = line[:index] + line[index+6:]
    return line

import re

import MeCab


def remove_after_item_number(line):
    # 商品番号の削除
    pattern = r"(?i)(商品番号|品番|型番|model)[：:\s]*[a-z0-9_-]+"
    match = re.search(pattern, line)
    if match:
        idx = match.start()
        line = line[:idx] + line[match.end():]
    return line.strip()

def remove_after_model_info(s):
    pattern = r"(?i)モデル.*"
    match = re.search(pattern, s)
    if match:
        s = s[:match.start()]
    return s

def remove_extra_info(s):
    pattern = r"[\s\S]*(?=さらにくわしい情報をみる)"
    match = re.match(pattern, s)
    if match:
        return match.group(0)
    return s

def remove_newlines(s):
    pattern = r"\r|\n"
    return re.sub(pattern, "", s)

wakati = MeCab.Tagger("-Owakati")

def remove_sentences_with_word(text):
    # ポイントを入れるのがどうか？
    words_to_remove = ["店舗", "※", "*", "＊",  "【", "購入",
                        "本体価格", "送料", "ポイント", 
                        "税込み", "全国", "特典", "商品番号",
                        "品番", "型番", "不良", "サービス",
                        "発送", "VIP", "税込", "無料", "返品",
                        "連絡", "無料" ]
    sentences = text.split('。')
    cleaned_sentences = []
    for sentence in sentences:
        sentence_words = wakati.parse(sentence).strip().split()
        should_remove = False
        for word in words_to_remove:
            if word in sentence_words:
                should_remove = True
                break
        if not should_remove:
            cleaned_sentences.append(sentence.strip())
    return '。'.join(cleaned_sentences)