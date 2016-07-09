#!/usr/bin/env python3

'''Create YAML for dashboard page by querying GitHub repositories.'''

import sys
import time
import yaml


CONTROLS = (
    ('swcarpentry/shell-novice', 'Unix Shell'),
    ('swcarpentry/git-novice', 'Git'),
    ('swcarpentry/hg-novice', 'Mercurial'),
    ('swcarpentry/sql-novice-survey', 'SQL'),
    ('swcarpentry/python-novice-inflammation', 'Python'),
    ('swcarpentry/r-novice-inflammation', 'R (Inflammation Data)'),
    ('swcarpentry/r-novice-gapminder', 'R (Gapminder Data)'),
    ('swcarpentry/matlab-novice-inflammation', 'MATLAB'),
    ('swcarpentry/make-novice', 'Make'),
    ('swcarpentry/capstone-novice-spreadsheet-biblio', 'From Excel to a Database via Python'),
    ('katyhuff/python-testing', 'Testing and Continuous Integration with Python'),
    ('DamienIrving/capstone-oceanography', 'Data Management in the Ocean, Weather and Climate Sciences'),
    ('swcarpentry/matlab-novice-capstone-biomed', 'Controlling a Quadcoptor With Your Mind'),
    ('swcarpentry/web-data-python', 'Working With Data on the Web'),
    ('swcarpentry/amy', 'Workshop Administration Tool'),
    ('swcarpentry/website', 'Software Carpentry Website'),
)


def get_connection(token_file):
    '''Get a connection to GitHub if the library and token file are available.'''
    try:
        from github import Github
    except:
        print('Unable to import github library', file=sys.stderr)
        sys.exit(1)
    try:
        with open(token_file, 'r') as reader:
            token = reader.read().strip()
    except:
        print('Unable to open token file "{0}"'.format(token_file), file=sys.stderr)
        sys.exit(1)
    return Github(token)


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
    for (ident, description) in CONTROLS:
        print('+', ident)
        dashboard['num_repos'] += 1
        r = cnx.get_repo(ident)
        record = {'ident' : ident,
                  'description' : description,
                  'url' : str(r.html_url)}
        record['pulls'], record['issues'] = filter(r.get_issues(state='open'))
        all_records.append(record)
    return dashboard


def filter(raw):
    '''Separate pull requests from issues.'''
    issues = []
    pulls = []
    for i in raw:
        try:
            entry = {'number' : i.number,
                     'title' : str(i.title),
                     'url' : str(i.html_url),
                     'updated' : i.updated_at.strftime('%Y-%m-%d')}
            if '/issues/' in entry['url']:
                issues.append(entry)
            elif '/pull/' in entry['url']:
                pulls.append(entry)
        except Exception as e:
            print('failed with', i.number, i.title, i.html_url, i.updated_at, file=sys.stderr)

    issues.sort(key=lambda x: x['updated'])
    pulls.sort(key=lambda x: x['updated'])
    return pulls, issues


def main():
    '''Main driver.'''
    token_file = sys.argv[1]
    output_file = sys.argv[2]
    cnx = get_connection(token_file)
    dashboard = process(cnx)
    with open(output_file, 'w') as writer:
        yaml.dump(dashboard, writer, encoding='utf-8', allow_unicode=True)

if __name__ == '__main__':
    main()
