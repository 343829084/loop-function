#!/bin/env python3

import loopfunction
from time import sleep


def target(x):
    print(x)
    sleep(2)

def on_stop(x='hello'):
    print('Stopped ' + x)

def on_start(x='hello'):
    print('Started ' + x)

loop_obj = loopfunction.Loop(target=target, args=('Hello, World!',),
                             on_start=on_start, on_start_args=('target', ),
                             on_stop=on_stop, on_stop_args=('target', ))
loop_obj.start()
