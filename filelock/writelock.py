import time

from filelock import (set_file_lock, is_locked, release_file_lock, FileLockError,
                      SetFileLockError)


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
                set_file_lock(self.filename)
                break
            except SetFileLockError("Can't set file lock."):
                if time.time() - start_time >= self.timeout:
                    raise FileLockError("A timeout occured!")
                time.sleep(self.delay)

    def release_lock(self):
        if is_locked:
            release_file_lock(self.filename)

    def __enter__(self):
        if not is_locked(self.filename):
            self.acquire_lock(self.filename)
            self.file = open(self.filename, self.mode)
            return self.file

    def __exit__(self):
        if is_locked(self.filename):
            self.release_lock()
            self.file.close()

    def __del__(self):
        self.release_lock(self.filename)
