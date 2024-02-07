#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = {}

    try:
        line_num = 0
        for line in sys.stdin:
            line_num += 1
            try:
                parts = line.split()
                size = int(parts[-1])
                status_code = parts[-2]
                total_size += size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

                if line_num % 10 == 0:
                    print_stats(total_size, status_counts)
            except ValueError:
                pass

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
