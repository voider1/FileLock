import time

from filelock import (set_write_lock, is_write_locked, release_write_lock,
                      FileLockError, SetFileLockError)


class WriteLock:
    def __init__(self, filename, mode, timeout=10, delay=0.5):
        self.filename = filename
        self.mode = mode
        self.timeout = timeout
        self.delay = delay
        self.file = None

    def acquire_lock(self, filename):
        start_time = time.time()

        while True:
            try:
                set_write_lock(self.filename)
                break
            except SetFileLockError:
                if time.time() - start_time >= self.timeout:
                    raise FileLockError("A timeout occured!")
                time.sleep(self.delay)

    def release_lock(self):
        if is_write_locked:
            release_write_lock(self.filename)

    def __enter__(self):
        self.acquire_lock(self.filename)
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        if is_write_locked(self.filename):
            if self.file is not None:
                self.file.close()

            self.release_lock()

    def __del__(self):
        if is_write_locked(self.filename):
            if self.file is not None:
                self.file.close()

            self.release_lock()
