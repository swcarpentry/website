#!/usr/bin/env python3
"""
Create skeleton of blog post about last week.

To run as stand-alone, ::

    $ week.py token
"""
import os
import sys
import getpass
from datetime import datetime

import git

TODAY = datetime.today()

FILEPATH = "_posts/{:%Y/%m}".format(TODAY)
FILENAME = "{:%Y-%m-%d}-weekly-update.html".format(TODAY)
FULLFILENAME = "{}/{}".format(FILEPATH, FILENAME)

HEADER = """---
layout: post
author: "{}"
title: "Weekly Update: {}"
date: {}
time: "{}"
category: ["Community"]
---
""".format(
        getpass.getuser(),
        TODAY.day,
        "{:%Y-%m-%d}".format(TODAY),
        "{:%H:%M:%S}".format(TODAY)
        )

def main():
    """
    Create the blog post.
    """
    print("Creating skeleton at {} ...".format(FULLFILENAME))
    if not os.path.isdir(FILEPATH):
        os.makedirs(FILEPATH)
    with open(FULLFILENAME, "w") as post:
        post.write(HEADER)
        post.write(git.generate_text())
    print("Skeleton created at {}.".format(FULLFILENAME))

if __name__ == "__main__":
    git.set_connection(sys.argv[1])
    main()
