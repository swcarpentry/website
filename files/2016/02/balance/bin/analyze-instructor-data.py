import sys

def main():

    seen, total_seen = {'F' : 0, 'M' : 0, 'O' : 0, 'U' : 0}, 0
    count, total_count = {'F' : 0, 'M' : 0, 'O' : 0, 'U' : 0}, 0

    for line in sys.stdin:
        name, gender, num = line.strip().split(',')
        num = int(num)
        seen[gender] += 1
        total_seen += 1
        count[gender] += num
        total_count += num

    print('gender,# people,% people,# taught,% taught')
    for g in 'FMOU':
        print('{0},{1},{2},{3},{4}'.format(g,
                                           seen[g], percent(seen[g], total_seen),
                                           count[g], percent(count[g], total_count)))


def percent(num, den):
    return round((100.0 * num) / den, 1)


if __name__ == '__main__':
   main()
