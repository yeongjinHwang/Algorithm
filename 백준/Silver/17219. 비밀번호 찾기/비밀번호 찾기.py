import sys
input = sys.stdin.readline

n,m = map(int,input().split())

sites = {}
for i in range(n) :
    site, password = input().split()
    sites[site] = password

find_pass = []
for i in range(m) :
    find_site = input().strip()
    find_pass.append(sites[find_site])

for i in find_pass :
    print(i)

