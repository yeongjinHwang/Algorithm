import sys

input = sys.stdin.readline

n = input()
p = list(map(int,input().split()))
sort_p = sorted(p)

result = []
for i in p :
    result.append(sort_p.index(i))
    sort_p[sort_p.index(i)] = -1

for i in result:
    sys.stdout.write(str(i)+' ')