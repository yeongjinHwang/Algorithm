import sys
input = sys.stdin.readline

n = list(map(int,input().split()))

listen = set()
for i in range(n[0]) :
    person = input().strip()
    listen.add(person)

view = set()
for j in range(n[1]) :
    person = input().strip()
    view.add(person)

listen_view = sorted(listen&view)

print(len(listen_view))
for i in listen_view :
    print(i)