#!/usr/bin/env pypy
import argparse
from algorithms import em1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="IBM models EM")
    parser.add_argument('source_file', type=str)
    parser.add_argument('destination_file', type=str)
    parser.add_argument('iterations', type=int)

    args = parser.parse_args()
    em1(args.source_file, args.destination_file, args.iterations)
