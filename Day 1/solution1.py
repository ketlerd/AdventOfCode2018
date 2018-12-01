import sys

freq = 0

file = open(sys.argv[1], 'r')

with open(sys.argv[1]) as f:
    for line in f:
        freq += int(line)

print(freq)