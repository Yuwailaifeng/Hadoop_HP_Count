#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

from operator import itemgetter
import sys

HPCount = {}

for line in sys.stdin:
    i = line.strip().split('\t')

    HPCount.setdefault(i[0],0)
    HPCount[i[0]] += int(i[1])

HP = {}
for k,v in HPCount.items():
    kk = k.split('#')
    HP.setdefault(kk[0],'')
    HP[kk[0]] += kk[1]+'|'+str(v)+';'

for k,v in HP.items():
    print(k + '\t' + v)
