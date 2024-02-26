import sys

def count_stats(file):
    lines = 0
    words = 0
    bytes_count = 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode('utf-8'))
    return lines, words, bytes_count

def print_stats(stats, end=" \n"):
        print(f"{stats[0]}\t{stats[1]}\t{stats[2]}", end=f"\t{end}\n")


if __name__ == "__main__":

    if len(sys.argv) == 1:
        lines = []
        for line in sys.stdin:
            if line == "\n":
                break
            else:
                lines.append(line)
        lines, words, bytes_count = count_stats(lines)
        print_stats([lines, words, bytes_count])

    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            print_stats(count_stats(file))

    else:
        total_lines = 0
        total_words = 0
        total_bytes = 0
        for filename in sys.argv[1:]:
            with open(filename, 'r', encoding='utf-8') as file:
                lines, words, bytes_count = count_stats(file)
                print_stats([lines, words, bytes_count], filename)
                print(f"\t{filename}")
                total_lines += lines
                total_words += words
                total_bytes += bytes_count
        if len(sys.argv) > 2:
            print_stats([total_lines, total_words, total_bytes], "total")


