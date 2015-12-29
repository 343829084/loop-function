#!/bin/env python3
import threading


class Loop:
    """Makes it easy for one function to go into an infinite loop
    some built in error handling
    """

    def __init__(self, target,
                 args=(), kwargs={},
                 on_stop=lambda: None):

        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.on_stop = on_stop

        self._stop_signal = False

        self._lock = threading.Event()
        self._lock.set()

        self.loop_thread = None

        self._in_subthread = None

    def _loop(self, *args, **kwargs):
        try:
            while not self._stop_signal:
                self.target(*args, **kwargs)
        finally:
            self._lock.set()
            self.on_stop()
            self._stop_signal = False

    def start(self, subthread=True):
        if self.is_running():
            raise RuntimeError('Loop is currently running')
        else:
            self._lock.clear()
            self._in_subthread = subthread
            if subthread:
                self.loop_thread = threading.Thread(target=self._loop,
                                                    args=self.args,
                                                    kwargs=self.kwargs)
                self.loop_thread.start()
            else:
                self._loop(*self.args, **self.kwargs)

    def stop(self):
        self.send_stop_signal()
        self._lock.wait()

    def send_stop_signal(self):
        if self.is_running():
            self._stop_signal = True

    def restart(self):
        if self._in_subthread is None:
            raise RuntimeError('A call to start must first be placed before restart')
        self.stop()
        in_subthread = self._in_subthread
        self.__init__(self.target, self.args, self.kwargs, self.on_stop)
        self.start(subthread=in_subthread)

    def is_running(self):
        return not self._lock.is_set()

