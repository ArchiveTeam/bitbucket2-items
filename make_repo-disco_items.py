import datetime
import sys

import zstandard


def main(start: str, end: str):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    with zstandard.open('repo-disco_{}-{}.txt.zst'.format(start.isoformat(), end.isoformat()), 'w') as f:
        while start < end:
            f.write('repo-disco:{}\n'.format(start.strftime('%Y-%m-%dT%H:%M')[:-1].replace(':', '%3A')))
            start += datetime.timedelta(minutes=30)

if __name__ == '__main__':
    main(*sys.argv[1:])

