#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# =============================================================================
# simple sampling 
# =============================================================================

# randomly choose k elements from N size lists of elements, with each element
# has a selected-probability k/n
# @k: k must be less than size N
# @N: list of elements with size N
def rand_sample(k, N):
    selectedNums=list()
    lenN = len(N)
    for i in range(lenN):
        if len(selectedNums) == k:
            break
        prob = (k-len(selectedNums)) / (lenN-i)
        # get a random number in [0.0, 1.0)
        if random.random() < prob:
            selectedNums.append(N[i])
    return selectedNums

list1 = [1,2,3,4,5,6,7,8,9,10,11]
print(rand_sample(5, list1))
