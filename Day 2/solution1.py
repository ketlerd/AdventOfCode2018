import sys

doubles = 0
triples = 0
countedDouble = False
countedTriple = False

visited = set()
duplicate = False

with open(sys.argv[1]) as f:
    for line in f:
        ls = list(line)
        for c in ls:
            if line.count(c) == 2 and c not in visited and not countedDouble:
                doubles = doubles + 1
                visited.add(c)
                countedDouble = True
            elif line.count(c) == 3 and c not in visited and not countedTriple:
                triples = triples + 1
                visited.add(c)
                countedTriple = True
        visited = set()
        countedDouble = False
        countedTriple = False

print(doubles * triples)