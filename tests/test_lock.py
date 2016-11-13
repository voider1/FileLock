#!venv/bin/python3

import pytest

from filelock import (set_read_lock, set_write_lock, set_readwrite_lock, ReadLock,
                      WriteLock, ReadWriteLock, FileLockError)


class TestLocks:
    filename = "test.txt"

    @pytest.fixture(scope="session", autouse=True)
    def setup(self, request):
        with open(self.filename, "w") as f:
            f.write("TEST123")

    def test_read_lock(self):
        set_read_lock(self.filename)
        with pytest.raises(FileLockError):
            with ReadLock(self.filename, "r", timeout=1, delay=0.5):
                pass

    def test_write_lock(self):
        set_write_lock(self.filename)
        with pytest.raises(FileLockError):
            with WriteLock(self.filename, "w", timeout=1, delay=0.5):
                pass

    def test_readwrite_lock(self):
        set_readwrite_lock(self.filename)
        with pytest.raises(FileLockError):
            with ReadWriteLock(self.filename, "rw", timeout=1, delay=0.5):
                pass
