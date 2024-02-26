import sys

def tail(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        last_lines = lines[-10:]
        for line in last_lines:
            print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 2:
        for file in sys.argv[1:]:
            print('==> {} <=='.format(file))
            tail(file)

    elif len(sys.argv) == 2:
        tail(sys.argv[1])
    else:
        lines = []
        for line in sys.stdin:
            if line == "\n":
                break
            else:
                lines.append(line)
        last_lines = lines[-17:]
        for line in last_lines:
            print(line, end='')