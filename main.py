#!/usr/bin/env python
import argparse
from algorithms import model1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="IBM models EM")
    parser.add_argument('source_file', type=str)
    parser.add_argument('destination_file', type=str)
    parser.add_argument('iterations', type=int)

    args = parser.parse_args()
    t = model1(args.source_file, args.destination_file, args.iterations)

    for translation, value in t.iteritems():
        if value >= 0.001:
            print("%s    %s    %.4f" % (translation + (value,)))
