statistical-machine-translation
===============================

IBM models implementation in python

## Performance tests ##
All tests done on 3K sentences with one iteration

1. python 2.7
```
$ time python main.py tests/sub-mini.en tests/sub-mini.pl 1 > out
```
Out:
```
real    0m45.607s
user    0m41.777s
sys     0m3.744s
```

2. python 3.3
```
$ time python3.3 main.py tests/sub-mini.en tests/sub-mini.pl 1 > out
```
Out:
```
real    0m52.923s
user    0m46.836s
sys     0m5.233s
```

3. pypy
```
$ time pypy main.py tests/sub-mini.en tests/sub-mini.pl 1 > out
```
Out:
```
real    1m11.052s
user    1m7.783s
sys     0m2.757s
```