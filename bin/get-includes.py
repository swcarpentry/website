#!/usr/bin/env python3

'''Fetch info about included files for display.'''

import sys
import os
import glob
import yaml

def main():
    '''Fetch info from disk and save as YAML.'''

    output_file = sys.argv[1]

    config = {
        'people' : get_relative('_includes/people/*.html', '_includes'),
        'projects' : get_relative('_includes/projects/*.html', '_includes')
    }

    with open(output_file, 'w') as writer:
        yaml.dump(config, writer, encoding='utf-8', allow_unicode=True)


def get_relative(file_pattern, to_subtract):
    return list(map(lambda x: os.path.relpath(x, to_subtract),
                    sorted(glob.glob(file_pattern))))


if __name__ == '__main__':
    main()
