from abc import ABCMeta, abstractmethod


class Lock(metaclass=ABCMeta):
    def __init__(self, filename, mode, timeout=10, delay=0.5):
        self.filename = filename
        self.mode = mode
        self.timeout = timeout
        self.delay = delay
        self.file = None

    @abstractmethod
    def acquire_lock(self, filename):
        pass

    @abstractmethod
    def release_lock(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass
