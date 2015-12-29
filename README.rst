============
loopfunction
============

Installation
============

::

    pip install loopfunction

or clone from `<https://github.com/Zaeb0s/loop-function>`_ and run

::

    python setup.py install

Usage
=====

Using the Loop class within loopfunction is similar to the Thread class within pythons threading module

The function::

    import loopfunction
    from time import sleep

    def function(x):
        print(x)
        sleep(2)

    loop_obj = loopfunction.Loop(target=function, args=('Hello, World!',))
    loop_obj.start()

Will print::

    >>> Hello, World!
    >>> Hello, World!
    >>> Hello, World!
    ...

loop_obj.stop(silent=False)
will

This will send a stop signal and then wait for the loop to stop

::

    loop_obj.send_stop_signal()


|-------------------------+------------------+
| Name                    | What does it do? |
|-------------------------+------------------+
| Loop.stop(silent=False) | Sends a stop signal if the  loop is running. Raises  RuntimeError if silent is  False and loop is not currently running. |

.. function::Loop.stop(silent=False)

