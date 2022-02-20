# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:04:59 2021

@author: sachin
"""


file = open(r"D:\OneDrive\Desktop\seq_sample.fasta", "r")

fasta = file.readlines()[1]  # NICE!

k = int(input("k: "))

d = dict()

for i in range(len(fasta)-k+1):
    seq = fasta[i:i+k]
    print(seq, end=',')

    # use .get instead d[seq] = d.get(seq, 0) + 1
    if seq in d:
        d[seq] += 1

    else:
        d[seq] = 1


# ANALYSIS AND OUTPUT


m = max(d.values())
print("\n\nMost freq kmers: ", end='')
for i in d:
    if d[i] == m:
        print(i, end=', ')
