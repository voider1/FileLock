FileLock
===========
A Python library for read and or write locking files.
Only write lock is supported for now, I'm still implementing the read and read write locks!
This library is **Python 3 focused**, and will **not work on Python 2**.
How to use?
--------------
Only WriteLock is supported for now!

```python
from filelock import WriteLock

with WriteLock("file.extension", "r", timeout=10, delay=0.5) as f:
    print(f.read())
```

Other WriteLocks will now try again every 0.5 seconds and stop when 10 seconds have passed. Then an error will be raised.
