# loopfunction
Makes it easy for one function to go into an infinite loop

## installation

```sh
pip install loopfunction
```

## Basics

```python
import loopfunction
from time import sleep

def function(x):
    print(x)
    sleep(2)

loop_obj = loopfunction.Loop(target=function, args=('Hello, World!',))
loop_obj.start()
```

This will output

```sh
Hello, World!
Hello, World!
Hello, World!
...
```

To stop

```python
loop_obj.stop()
```

For a more in deapth explanation of each function see the docstrings
in [loopfunction.py](https://github.com/Zaeb0s/loop-function/blob/master/loopfunction/loopfunction.py)