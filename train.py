import sys
import tomotopy as tp

"""
HYPER PARAMETERS
"""
TOPIC_NUM = 10
MIN_CF = 10000
RM_TOP = 10
BURN_IN = 3000


def lda_example(lines, save_path):
    # mdl = tp.LDAModel(tw=tp.TermWeight.ONE, min_cf=MIN_CF, rm_top=RM_TOP, k=TOPIC_NUM)
    mdl = tp.CTModel(tw=tp.TermWeight.ONE, min_cf=MIN_CF, rm_top=RM_TOP, k=TOPIC_NUM)
    for line in lines:
        ch = line.strip().split()
        if len(ch) == 0:
            continue
        mdl.add_doc(ch)
    mdl.burn_in = BURN_IN
    mdl.train(0)
    print('Num docs:', len(mdl.docs), ', Vocab size:', len(mdl.used_vocabs), ', Num words:', mdl.num_words)
    print('Removed top words:', mdl.removed_top_words)
    print('Training...', file=sys.stderr, flush=True)
    for i in range(0, 3000, 20):
        mdl.train(20)
        print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))
    
    mdl.summary()
    print('Saving...', file=sys.stderr, flush=True)
    mdl.save(save_path, True)

    for k in range(mdl.k):
        print('Topic #{}'.format(k))
        for word, prob in mdl.get_topic_words(k):
            print('\t', word, prob, sep='\t')

# You can get the sample data file 'enwiki-stemmed-1000.txt'
# at https://drive.google.com/file/d/18OpNijd4iwPyYZ2O7pQoPyeTAKEXa71J/view?usp=sharing
with open('data/train.txt', 'r', encoding="utf-8") as f:
    input_lines = f.read().splitlines()
print('Running LDA')
lda_example(input_lines, f'pa-T-{TOPIC_NUM}-M-{MIN_CF}-R-{RM_TOP}-B-{BURN_IN}.bin')
