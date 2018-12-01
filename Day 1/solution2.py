import sys

freq = 0
results = set()
duplicate = False

while duplicate != True:
    with open(sys.argv[1]) as f:
        for line in f:
            freq += int(line)

            if freq in results:
                duplicate = True
                break

            results.add(freq)
print(freq)