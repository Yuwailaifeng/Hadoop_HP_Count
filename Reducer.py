#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

from operator import itemgetter
import sys

HP = {}
for line in sys.stdin:
    word, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    HP.setdefault(word,0)
    HP[word] += count


HPCount = {}
for k,v in HP.items():
    disease, hp = k.split('#')
    HPCount.setdefault(disease,'')
    HPCount[disease] += hp+'|'+str(v)+';'

for k,v in HPCount.items():
    print(k + '\t' + v)
