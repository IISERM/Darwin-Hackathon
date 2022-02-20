# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:05:00 2021

@author: sachin
"""
#   Either my code is wrong or the distribution of genotype is the same
#   every time. Either way I'm angry.

# evaluators note - LOL

import numpy
# dictionary:


#    {..(0,0):[<0,0>,<1,1>]....}
gens = int(input("gens: "))
N = int(input("N: "))

lookup = {
    0: (0.25, 0.25, 0, 0.25, 0.25, 0, 0, 0, 0),
    1: (0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0, 0, 0),
    2: (0, 0.25, 0.25, 0, 0.25, 0.25, 0, 0, 0),
    3: (0.125, 0.125, 0, 0.25, 0.25, 0, 0.125, 0.125, 0),
    4: (0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625),
    5: (0, 0.125, 0.125, 0, 0.25, 0.25, 0, 0.125, 0.125),
    6: (0, 0, 0, 0.25, 0.25, 0, 0.25, 0.25, 0),
    7: (0, 0, 0, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125),
    8: (0, 0, 0, 0, 0.25, 0.25, 0, 0.25, 0.25)
}

pltn = [0, 0, 0, 0, 1, 0, 0, 0, 0]

for i in range(gens):
    p = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for j in range(9):
        babies = lookup[j]  # nice variable name XD
        for k in range(9):
            p[k] += 2*pltn[j]*babies[k]

    pltn = p

prob = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    prob[i] = pltn[i]/2**gens

i = 0
count_N = 0
preci = 10000  # precision

while(i < preci):
    j = 0
    count_gtp4 = 0
    while j < 2**gens:
        count_gtp4 += numpy.random.choice([0, 1], p=[0.75, 0.25])
        j += 1

    # print('iter')

    if count_gtp4 >= N:
        count_N += 1

    i += 1


print(count_N/preci)
