def preprocessing(line):
    line = remove_bracket(line)
    line = remove_item_description(line)
    line = remove_sentence_after_footnote(line)
    return line

def remove_bracket(line):
    index = line.find("【")  # "【" のインデックスを検索する
    if index != -1:  # "【"が見つかった場合
        line = line[:index]  # "【"より前の部分を取得する
    return line

def remove_item_description(line):
    # アイテム説明のインデックスを検索
    index = line.find("アイテム説明")
    if index != -1:
        # アイテム説明の前のテキストとアイテム説明以降のテキストを連結する
        line = line[:index] + line[index+6:]
    return line


def remove_sentence_after_footnote(line):
    # テキスト中の「※」を検索
    index = line.find("※")
    if index != -1:
        # 「※」以降の一文を検索
        period_index = line.find("。", index)
        if period_index != -1:
            # 「※」以降の一文を削除
            line = line[:index] + line[period_index+1:]
        else:
            # 「※」以降に文末がない場合は、全体を削除
            line = line[:index]
    return line
