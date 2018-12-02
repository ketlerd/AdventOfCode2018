import sys

result = set()
string = ""
count = 0
character = ''

with open(sys.argv[1]) as f:
    for line in f:
        with open(sys.argv[1]) as f2:
            for line2 in f2:
                for x in range(len(line)):
                    if line[x] != line2[x]:
                        if line[x] not in result:
                            result.add(line[x])
                if len(result) == 1:
                    character = result.pop()
                    if line.count(character) > 1:
                        break
                    print(line.replace(character, ''))
                    break
                
                result = set()


