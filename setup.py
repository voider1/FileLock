#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="File Lock",
    packages=["filelock"],
    version="0.1",
    description="A module for read and or write locking files.",
    author="Wesley A. Gahr",
    author_email="wesleyey0408@gmail.com",
    download_url="https://github.com/voider1/FileLock",
    keywords=["file lock", "read lock", "write lock", "read/write lock"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD-3-Clause",
        "Environment :: Other Environment",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: File Locking :: File Writing"
    ],
    long_description="""
    File locking
    ------------

    A module for read and or write locking files, no corrupt files anymore!
    """
)
