import sys
from datetime import datetime
from github import Github

DATE_FORMAT = '%Y-%m-%d'

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    try:
        start_date = datetime.strptime(sys.argv[3], DATE_FORMAT)
        end_date = datetime.strptime(sys.argv[4], DATE_FORMAT)
    except ValueError as e:
        print(e)
        sys.exit(1)
    all_repos = sys.argv[5:]

    cnx = Github(username, password)
    events = []
    for repo in all_repos:
        print('{0}...'.format(repo), file=sys.stderr)
        events += get_events(cnx, repo, start_date, end_date)

    for (repo, name, created, kind) in events:
        print('{0},{1},{2},{3}'.format(repo, name, created, kind))

def get_events(connection, repo, start_date, end_date):
    '''Get events from GitHub repository.'''
    events = connection.get_repo(repo).get_events()
    out = [(repo, e.actor.name, e.created_at.strftime(DATE_FORMAT), e.type)
           for e in events
           if e.actor.name and (start_date <= e.created_at <= end_date)]
    return out

if __name__ == '__main__':
    main()
