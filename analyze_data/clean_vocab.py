import json

with open('./vocab.json', 'r', encoding='shift-jis') as f:
    vocab_dict = json.load(f)

new_vocab_dict = {}
for k in vocab_dict.keys():
    if vocab_dict[k] > 70000:
        new_vocab_dict[k] = vocab_dict[k]

with open('./clean_vocab.json', 'w', encoding='shift-jis') as f:
    json.dump(new_vocab_dict, f, ensure_ascii=False)