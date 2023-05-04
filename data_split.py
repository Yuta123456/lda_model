
import glob
import pandas as pd
import random
filepaths = glob.glob("D:/M1/fashion/IQON/IQON3000/**/**/*_new.json")
test = []
train = []
for fp in filepaths:
    if random.random() < 0.3:
        test.append(fp)
    else:
        train.append(fp)
with open("data/test.txt", mode="w", encoding="utf-8") as f:
    f.write("\n".join(test))
with open("data/train.txt", mode="w", encoding="utf-8") as f:
    f.write("\n".join(train))