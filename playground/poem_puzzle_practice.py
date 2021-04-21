import re
from glob import iglob
from itertools import chain

from toolz.functoolz import pipe

# interchange with Counter and frequencies
from collections import Counter
from toolz import frequencies


class PoemCleaner:
    def __init__(self):
        self.r = re.compile(r"[.,;:!-]")

    def clean_poem(self, fp):
        with open(fp) as poem:
            no_punch = self.r.sub(" ", poem.read())
            return no_punch.lower().split()


def function_word_or_not(word):
    return word in ["a", "the"]


def word_ratio(d):
    return float(d.get("a", 0)) / float(d.get("the", 0.0001))


## self practice
def filterandlist(tokens, func=function_word_or_not):
    return list(filter(func, tokens))


# simple practice with from toolz.functoolz import pipe
def tokens2ratio(tokens):
    return pipe(tokens, filterandlist, Counter, word_ratio)


if __name__ == "__main__":

    cleaner = PoemCleaner()

    authora_poems = iglob(
        "/home/nghiaht/pyspark/mastering-large-datasets/Ch04/author_a/*.txt"
    )
    authorb_poems = iglob(
        "/home/nghiaht/pyspark/mastering-large-datasets/Ch04/author_b/*.txt"
    )

    tokens_a = chain(*map(cleaner.clean_poem, authora_poems))
    ratio_a = word_ratio(Counter(filter(function_word_or_not, tokens_a)))
    print(ratio_a)

    # maybe chain (itertool) or iglob is single-use iterator --> recreate tokens
    authora_poems = iglob(
        "/home/nghiaht/pyspark/mastering-large-datasets/Ch04/author_a/*.txt"
    )
    tokens_a = chain(*map(cleaner.clean_poem, authora_poems))
    ratio_a2 = tokens2ratio(tokens_a)
    print(ratio_a2)

    tokens_b = chain(*map(cleaner.clean_poem, authorb_poems))
    ratio_b = tokens2ratio(tokens_b)
    print(ratio_b)
