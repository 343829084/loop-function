#!/bin/env python3

import loopfunction
from time import sleep


def function(x):
    print(x)
    sleep(2)

loop_obj = loopfunction.Loop(target=function, args=('Hello, World!',))
loop_obj.start()

