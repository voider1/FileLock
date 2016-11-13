import time

from filelock import (set_readwrite_lock, is_readwrite_locked,
                      release_readwrite_lock, FileLockError, SetFileLockError)
from filelock.lock import Lock


class ReadWriteLock(Lock):
    """A read and write lock class, use as a context manager
       Makes sure only one process can write to it."""

    def acquire_lock(self, filename):
        """Tries to lock the file for writing."""

        start_time = time.time()

        while True:
            try:
                set_readwrite_lock(self.filename)
                break
            except SetFileLockError as e:
                if time.time() - start_time >= self.timeout:
                    raise FileLockError(e)
                time.sleep(self.delay)

    def release_lock(self):
        """Remove the lock from the file and close file for reading/writing."""

        if is_readwrite_locked(self.filename):
            if self.file is not None:
                self.file.close()
            release_readwrite_lock(self.filename)

    def __enter__(self):
        """Give back a file when entering the context and put a lock on it."""

        self.acquire_lock(self.filename)
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        """Remove the lock from the file and close the file."""

        self.release_lock()

    def __del__(self):
        """Make sure there are no lingering locks."""

        self.release_lock()
