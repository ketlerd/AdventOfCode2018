import sys

freq = 0

with open(sys.argv[1]) as f:
    for line in f:
        freq += int(line)

print(freq)