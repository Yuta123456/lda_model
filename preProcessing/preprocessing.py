def preprocessing(line, debug=False):
    preprocesser = [remove_bracket, remove_item_description,
                     remove_sentence_after_footnote, remove_after_item_number,
                       remove_after_contact_info, remove_after_model_info, remove_extra_info]
    # 最後に追加
    preprocesser.append(remove_newlines)
    for p in preprocesser:
        line = p(line)
        if debug:
            print(f"{p.__name__}",line)
    return line

def remove_bracket(line):
    while True:
        start_index = line.find("【")
        if start_index == -1:
            break
        end_index_period = line.find("。", start_index)
        end_index_newline = line.find("\r\n", start_index)
        if end_index_period == -1:
            end_index = end_index_newline
        elif end_index_newline == -1:
            end_index = end_index_period
        else:
            end_index = min(end_index_period, end_index_newline)
        if end_index == -1:
            break
        line = line[:start_index] + line[end_index + 1:]
    return line.strip()

def remove_item_description(line):
    # アイテム説明のインデックスを検索
    index = line.find("アイテム説明")
    if index != -1:
        # アイテム説明の前のテキストとアイテム説明以降のテキストを連結する
        line = line[:index] + line[index+6:]
    return line

import re


def remove_after_item_number(line):
    # 商品番号の削除
    pattern = r"(?i)(商品番号|品番|型番|model)[：:\s]*[a-z0-9_-]+"
    match = re.search(pattern, line)
    if match:
        idx = match.start()
        line = line[:idx] + line[match.end():]
    return line.strip()



def remove_sentence_after_footnote(line):
    while True:
        # テキスト中の「※」または「＊」を検索
        index1 = line.find("※")
        index2 = line.find("＊")
        if index1 != -1 and (index2 == -1 or index1 < index2):
            # 「※」以降の一文を検索
            period_index = line.find("。", index1)
            if period_index != -1:
                # 「※」以降の一文を削除
                line = line[:index1] + line[period_index+1:]
            else:
                # 「※」以降に文末がない場合は、全体を削除
                line = line[:index1]
        elif index2 != -1 and (index1 == -1 or index2 < index1):
            # 「＊」以降の一文を検索
            period_index = line.find("。", index2)
            if period_index != -1:
                # 「＊」以降の一文を削除
                line = line[:index2] + line[period_index+1:]
            else:
                # 「＊」以降に文末がない場合は、全体を削除
                line = line[:index2]
        else:
            break
    return line



def remove_after_model_info(s):
    pattern = r"(?i)モデル.*"
    match = re.search(pattern, s)
    if match:
        s = s[:match.start()]
    return s

def remove_after_contact_info(s):
    pattern1 = r"(?i)店舗へのお問い合わせ.*"
    pattern2 = r"店舗へお問い合わせの際は下記品番をお伝えください。.*"
    
    match1 = re.search(pattern1, s)
    match2 = re.search(pattern2, s)
    
    if match1:
        s = s[:match1.start()]
    elif match2:
        s = s[:match2.start()]
        
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