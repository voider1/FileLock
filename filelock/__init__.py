class FileLockError(Exception):
    pass


class SetFileLockError(Exception):
    pass


def lock_factory():
    write_locked_files = set([])

    def set_write_lock(filename):
        nonlocal write_locked_files
        if filename in write_locked_files:
            raise SetFileLockError("File is already locked!")
        write_locked_files.add(filename)

    def is_write_locked(filename):
        nonlocal write_locked_files
        return filename in write_locked_files

    def release_write_lock(filename):
        nonlocal write_locked_files
        write_locked_files.remove(filename)

    return (set_write_lock, is_write_locked, release_write_lock)


set_write_lock, is_write_locked, release_write_lock = lock_factory()

from filelock.writelock import WriteLock
