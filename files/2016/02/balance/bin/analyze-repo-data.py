import sys

def main():

    genders = read_genders(sys.argv[1])
    known_people = set()
    seen, total_seen = {}, 0
    count, total_count = {}, 0

    for line in sys.stdin:
        repo, name, date, kind = line.strip().split(',')

        if name in genders:
            g = genders[name]
        else:
            print(name, file=sys.stderr)
            g = 'U'

        count[g] = count.get(g, 0) + 1
        total_count += 1
        if name not in known_people:
            known_people.add(name)
            seen[g] = seen.get(g, 0) + 1
            total_seen += 1

    all_genders = seen.keys()
    print('gender,# people,% people,# contrib, % contrib')
    for g in all_genders:
        print('{0},{1},{2},{3},{4}'.format(g,
                                           seen[g], percent(seen[g], total_seen),
                                           count[g], percent(count[g], total_count)))

def read_genders(filename):
    '''Read gender,name pairs.'''

    result = {}
    with open(filename, 'r') as reader:
        for line in reader:
            gender, name = line.strip().split(',', 1)
            result[name] = gender

    return result

def percent(num, den):
    return round((100.0 * num) / den, 1)

if __name__ == '__main__':
    main()
