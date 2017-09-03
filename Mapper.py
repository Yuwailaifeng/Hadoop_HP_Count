#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    i = line.strip().split('\t')[0:4]
    print(i[1]+'#'+i[3] + '\t' + str(1))
