import time

from filelock import (set_read_lock, is_read_locked, release_read_lock,
                      FileLockError, SetFileLockError)
from filelock.lock import Lock


class ReadLock(Lock):
    """A read lock class, use as a context manager
       Makes sure only one process can write to it."""

    def acquire_lock(self, filename):
        """Tries to lock the file for writing."""

        start_time = time.time()

        while True:
            try:
                set_read_lock(self.filename)
                break
            except SetFileLockError:
                if time.time() - start_time >= self.timeout:
                    raise FileLockError("A timeout occured!")
                time.sleep(self.delay)

    def release_lock(self):
        """Remove the lock from the file and close file for reading/writing."""

        if is_read_locked(self.filename):
            if self.file is not None:
                self.file.close()
            release_read_lock(self.filename)

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
