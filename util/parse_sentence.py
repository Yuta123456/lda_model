import MeCab

wakati = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger()

def parse_sentence(sentence):
    parsed = wakati.parse(sentence).strip().split()
    node = tagger.parseToNode(sentence)
    node = node.next
    result = []
    for w in parsed:
        if (not node):
            continue
        hinshi = node.feature.split(",")[0]
        result.append((w, hinshi))
        node = node.next
        
    return result