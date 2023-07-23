with open('D:\M1/fashion/lda_model/data/fashion_clip.txt', mode="r", encoding="utf-8") as f:
    data = f.read().splitlines()
item_info = {}
for i in data:
    i = i.strip()
    item_id, category, color = i.split(' ')