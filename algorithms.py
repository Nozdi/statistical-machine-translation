"""
.. module:: algorithms
    :synopsis: Module which contains IBM Models algorithms
"""
import operator
import math
from decimal import Decimal
from collections import defaultdict
from itertools import (
    chain,
    izip,
)


def load_sentences(source_file, destination_file):
    with open(source_file) as source, open(destination_file) as destination:
        e = [line.lower().split() for line in destination]
        f = [line.lower().split() + ["NULL"] for line in source]

    return e, f


def perplexity(t, e_sentences, f_sentences, eps=1.):
    probabilities = []
    for e_words, f_words in izip(e_sentences, f_sentences):
        probabilities.append(
            eps/(len(f_words)**len(e_words)) *
            reduce(
                operator.mul,
                [sum([t[(f, e)] for f in f_words]) for e in e_words]
            )
        )
    return 2 ** Decimal(-sum(map(lambda x: math.log(x, 2), probabilities)))


def model1(source_file, destination_file, iterations):
    # initialization
    e_sentences, f_sentences = load_sentences(source_file, destination_file)

    all_e_words = set(chain(*e_sentences))
    all_f_words = set(chain(*f_sentences))

    t = defaultdict(lambda: 0.25)

    for _ in xrange(iterations):
        count = defaultdict(float)
        total = defaultdict(float)
        s_total = defaultdict(float)

        for e_words, f_words in izip(e_sentences, f_sentences):
            # compute normalization
            for e in e_words:
                s_total[e] = 0
                for f in f_words:
                    s_total[e] += t[(f, e)]

            # collect counts
            for e in e_words:
                for f in f_words:
                    counts = t[(f, e)]/s_total[e]
                    count[(f, e)] += counts
                    total[f] += counts

        # estimate probabilities
        for f in all_f_words:
            for e in all_e_words:
                t[(f, e)] = count[(f, e)]/total[f]

    return t, perplexity(t, e_sentences, f_sentences)
