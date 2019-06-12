#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class ReservoirSampling(object):
    
    # choose K elements from a unknown length of data stream, 
    # where each element has a k/N probability to enter the selected reservoir
    # N is the length of the current data stream.
    # Assume N >> k
    
    def __init__(self, K):
        self.reservoir = []
        self.sizeK = K
        self.N = 0
        
    # a new element coming from the data stream
    # this new element has k/n probability entering the reservoir
    def get_next_element(self, newEle):
        
        # add first k elements into the reservoir
        if len(self.reservoir) < self.sizeK:
            self.reservoir.append(newEle)
        else:
            # for every new element,put this element into the reservoir with prob = k/N
            # choose a integer from [0,N-1]
            j = random.randint(0,self.N-1)
            if j < self.sizeK:
                self.reservoir[j] = newEle
        self.N += 1
            
            
            
        
        
    