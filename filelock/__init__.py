class FileLockError(Exception):
    pass


class SetFileLockError(Exception):
    pass


def lock_factory():
    locked_files = set([])

    def set_lock(filename):
        nonlocal locked_files
        if filename in locked_files:
            raise SetFileLockError("The file is already locked!")
        locked_files.add(filename)

    def is_locked(filename):
        nonlocal locked_files
        return filename in locked_files

    def release_lock(filename):
        nonlocal locked_files
        locked_files.remove(filename)

    return (set_file_lock, is_file_locked, release_file_lock)


set_file_lock, is_file_locked, release_file_lock = lock_factory()

import writelock
