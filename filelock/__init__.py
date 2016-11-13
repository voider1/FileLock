class FileLockError(Exception):
    pass


class SetFileLockError(Exception):
    pass


def lock_factory():
    write_locked_files = set([])
    read_locked_files = set([])

    def set_write_lock(filename):
        nonlocal write_locked_files
        if filename in write_locked_files:
            raise SetFileLockError("File is already write locked!")
        write_locked_files.add(filename)

    def is_write_locked(filename):
        nonlocal write_locked_files
        return filename in write_locked_files

    def release_write_lock(filename):
        nonlocal write_locked_files
        try:
            write_locked_files.remove(filename)
        except KeyError:
            raise ValueError("File is not write locked.")

    def set_read_lock(filename):
        nonlocal read_locked_files
        if filename in read_locked_files:
            raise SetFileLockError("File is already read locked!")
        read_locked_files.add(filename)

    def is_read_locked(filename):
        nonlocal read_locked_files
        return filename in read_locked_files

    def release_read_lock(filename):
        nonlocal read_locked_files
        try:
            read_locked_files.remove(filename)
        except KeyError:
            raise ValueError("File is not read locked.")

    def set_readwrite_lock(filename):
        set_read_lock(filename)
        set_write_lock(filename)

    def is_readwrite_locked(filename):
        is_read_locked(filename)
        is_write_locked(filename)

    def release_readwrite_lock(filename):
        release_read_lock(filename)
        release_write_lock(filename)

    return (set_write_lock, is_write_locked, release_write_lock, set_read_lock,
            is_read_locked, release_read_lock, set_readwrite_lock,
            is_readwrite_locked, release_readwrite_lock)


set_write_lock, is_write_locked, release_write_lock, set_read_lock, \
        is_read_locked, release_read_lock, set_readwrite_lock, \
        is_readwrite_locked, release_readwrite_lock = lock_factory()

from filelock.readwritelock import ReadWriteLock
from filelock.readlock import ReadLock
from filelock.writelock import WriteLock
