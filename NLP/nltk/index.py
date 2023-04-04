from nlp import FreqDist
from nlp.corpus import brown
print(brown.categories())
new_text = brown.words(categories='humor')
fDist = FreqDist([w.lower() for w in new_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'yes']

for m in modals:
    print('%s : %d' % (m, fDist[m]))
