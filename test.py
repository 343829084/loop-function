#!/bin/env python3

import loopfunction
from time import sleep

def p():
    print('Hi')
    sleep(2)

x = loopfunction.Loop(target=p)
