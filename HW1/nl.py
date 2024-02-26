import sys

def nl(file):
    n = 1
    for line in file:
        print(f"{n}\t{line}", end="")
        n += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            nl(file)
    else:
        nl(sys.stdin)