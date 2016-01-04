#!/usr/bin/env python3
"""
Wrap up around GitHub.
"""
from github import Github
# If you need to debug,
# uncomment the next line will help.
# github.enable_console_debug_logging()

CONTROLS = (
    ('swcarpentry/shell-novice', 'Unix Shell'),
    ('swcarpentry/git-novice', 'Git'),
    ('swcarpentry/hg-novice', 'Mercurial'),
    ('swcarpentry/sql-novice-survey', 'SQL'),
    ('swcarpentry/python-novice-inflammation', 'Python'),
    ('swcarpentry/r-novice-inflammation', 'R'),
    ('swcarpentry/matlab-novice-inflammation', 'MATLAB'),
    ('swcarpentry/make-novice', 'Make'),
    ('swcarpentry/capstone-novice-spreadsheet-biblio', 'From Excel to a Database via Python'),
    ('katyhuff/python-testing', 'Testing and Continuous Integration with Python'),
    ('DamienIrving/capstone-oceanography', 'Data Management in the Ocean, Weather and Climate Sciences'),
    ('swcarpentry/matlab-novice-capstone-biomed', 'Controlling a Quadcoptor With Your Mind'),
    ('swcarpentry/web-data-python', 'Working With Data on the Web'),
    ('swcarpentry/amy', 'Workshop administration tool'),
    ('swcarpentry/website', 'Software Carpentry website'),
)

def get_connection(token_file):
    '''Get a connection to GitHub if the library and token file are available.'''
    try:
        with open(token_file, 'r') as reader:
            token = reader.read().strip()
    except:
        print('Unable to open token file "{0}"'.format(token_file), file=sys.stderr)
        sys.exit(1)
    return Github(token)
