import names
import progressbar
import argparse

FIRSTNAMES = []
LASTNAMES =  []
with open(names.FILES['first:female']) as f:
    for line in f.readlines():
        FIRSTNAMES.append(line.split(' ')[0])
with open(names.FILES['first:male']) as f:
    for line in f.readlines():
        FIRSTNAMES.append(line.split(' ')[0])
with open(names.FILES['last']) as f:
    for line in f.readlines():
        LASTNAMES.append(line.split(' ')[0])

def word_divider(word, other):
    nword = []
    other = list(other)
    for l in word:
        if l in other:
            nword.append(l)
            other.remove(l)
        else:
            return False
    return (''.join(nword), ''.join(other))

def name_anagramer(name):
    out = []
    name = ''.join(name.split()).upper()
    pbar = progressbar.ProgressBar(max_value=len(FIRSTNAMES)).start()
    for fn in FIRSTNAMES:
        r = word_divider(fn, name)
        if r:
            for ln in LASTNAMES:
                if sorted(r[1]) == sorted(ln):
                    out.append('{first} {last}'.format(first=r[0], last=ln))
        pbar += 1
    pbar.finish()
    return out

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')

    args = parser.parse_args()
    print(name_anagramer(args.name))
