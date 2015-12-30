#!/usr/bin/env bash

## Rebuild the web site on the software-carpentry.org server.

# Update, overwriting local changes.
cd ~/projects/website
git fetch --all
git reset --hard origin/gh-pages

# Switch to the local installation of Python 3.
source ~/drd_python/venv.amy.p3/bin/activate

# Rebuild data files.
make amy
make dashboard
make includes

# Rebuild the site.
jekyll build

# Install.
rm -rf ~/sites/software-carpentry.org/*
mv ~/projects/website/_site/* ~/sites/software-carpentry.org
