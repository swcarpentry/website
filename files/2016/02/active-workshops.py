import sys
import yaml
from datetime import date, timedelta

data = yaml.load(sys.stdin)
workshops = data['workshops_past'] + data['workshops_current']
start = min(w['start'] for w in workshops)
end = max(w['end'] for w in workshops if w['end'] is not None)

day = timedelta(1, 0, 0)
current = start
count = {}
while current <= end:
    count[current] = 0
    current += day

for w in workshops:
    if w['end'] is None:
        count[w['start']] += 1
    else:
        current = w['start']
        while current <= w['end']:
            count[current] += 1
            current += day

current = start
while current <= end:
    print('{0},{1}'.format(current.isoformat(), count[current]))
    current += day
