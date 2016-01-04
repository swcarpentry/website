#!/usr/bin/env python3
'''
Create YAML for dashboard page by querying GitHub repositories.

Usage::

    $ python3 dashboard.py token-file output-file
'''
import sys
import time
import yaml

import git

def process(cnx):
    '''Gather information.'''
    if not cnx:
        return []
    all_records = []
    dashboard = {
        'records' : all_records,
        'num_repos' : 0,
        'num_issues' : 0,
        'timestamp' : time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    }
    for (ident, description) in git.CONTROLS:
        print('+', ident)
        dashboard['num_repos'] += 1
        r = cnx.get_repo(ident)
        record = {'ident' : ident,
                  'description' : description,
                  'url' : str(r.html_url),
                  'issues' : []}
        all_records.append(record)
        for i in r.get_issues(state='open'):
            try:
                record['issues'].append({'number' : i.number,
                                         'title' : str(i.title),
                                         'url' : str(i.html_url),
                                         'updated' : i.updated_at.strftime('%Y-%m-%d')})
            except Exception as e:
                print('failed with', i.number, i.title, i.html_url, i.updated_at, file=sys.stderr)
            dashboard['num_issues'] += 1
        record['issues'].sort(key=lambda x: x['updated'])
    return dashboard

def main():
    '''Main driver.'''
    token_file = sys.argv[1]
    output_file = sys.argv[2]
    cnx = git.get_connection(token_file)
    dashboard = process(cnx)
    with open(output_file, 'w') as writer:
        yaml.dump(dashboard, writer, encoding='utf-8', allow_unicode=True)

if __name__ == '__main__':
    main()
