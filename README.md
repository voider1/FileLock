FileLock
===========
A Python library for read and or write locking files.
This library is **Python 3 focused**, and will **not work on Python 2**.
How to use?
--------------

```python
from filelock import ReadLock, WriteLock, ReadWriteLock

with ReadLock("file.extension", "r", timeout=10, delay=0.5) as f:
    print(f.read())
    
with WriteLock("file.extension", "r", timeout=10, delay=0.5) as f:
    print(f.read())

with ReadWriteLock("file.extension", "r", timeout=10, delay=0.5) as f:
    print(f.read())
```

Other Locks will wait until the first Lock is finished for 10 seconds and will retry every 0.5 seconds. The values I've defined are standard, so normally you could just leave them out if you're fine with the defaults like so:
```python
from filelock import ReadLock

with ReadLock("file.extension", "r") as f:
    print(f.read())
```
