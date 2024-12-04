import sys
input = sys.stdin.readline

n,m = map(int, input().split())
poke_value_name = {}
poke_value_num = {}

for i in range(n):
    name = input().strip()
    poke_value_name[i] = name
    poke_value_num[name] = i

for i in range(m):
    find = input().strip()
    if find[0].isalpha():
        print(poke_value_num[find]+1)
    else:
        print(poke_value_name[int(find)-1])
