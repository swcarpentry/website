#!/usr/bin/env python3

'''Fetch info about workshops, airports, etc. from AMY.'''

import sys
import time
import datetime
import ssl
import urllib.request
import yaml

def main():
    '''
    Fetch information and store in one YAML file.
    '''

    # Controls.
    amy_url = sys.argv[1]
    output_file = sys.argv[2]

    # Get stock information from AMY.
    config = {
        'timestamp' : time.strftime('%Y%m%dT%H%M%SZ', time.gmtime()),
        'badges' : fetch_info(amy_url, 'export/badges.yaml'),
        'airports' : fetch_info(amy_url, 'export/instructors.yaml')
    }

    # Adjust.
    config['workshops_past'], config['workshops_current'] = \
        split_workshops(fetch_info(amy_url, 'events/published.yaml'), \
                                   datetime.date.today())
    config['workshops'] = [config['workshops_past'], config['workshops_current']]

    # Coalesce flag information.
    config['flags'] = {
        'workshops': sort_flags(config['workshops_past']),
        'airports': sort_flags(config['airports'])
    }

    # Save.
    with open(output_file, 'w') as writer:
        yaml.dump(config, writer, encoding='utf-8', allow_unicode=True)


def fetch_info(base_url, url):
    '''Download and save data.'''

    address = base_url + url

    which_python = sys.version_info[:3]
    if which_python <= (3, 4, 2):
        with urllib.request.urlopen(address) as f:
            content = f.read()
    else:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        with urllib.request.urlopen(address, context=ssl_context) as f:
                content = f.read()

    return yaml.load(content.decode('utf-8'))


def split_workshops(workshops, today):
    '''Split workshops into past and current.'''

    past = []
    current = []
    for w in workshops:
        sort_date = w['end'] if w['end'] else w['start']
        if sort_date < today:
            past.append(w)
        else:
            current.append(w)
    return past, current


def sort_flags(data):
    '''Create sorted list of unique flags, lower-casing as a side effect.'''

    for entry in data:
        entry['country'] = entry['country'].lower()
    return sorted({entry['country'] for entry in data if entry['country']})


if __name__ == '__main__':
    main()
