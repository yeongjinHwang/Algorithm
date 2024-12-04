import sys
input = sys.stdin.readline

m = int(input().strip())

s = set()
for i in range(m) :
    cal = input().split()
    if len(cal) == 2 : cal[1] = int(cal[1])
    if cal[0] == "add" : s.add(cal[1])
    elif cal[0] == "remove" : s.discard(cal[1])
    elif cal[0] == "check" : 
        if cal[1] in s : print(1)
        else : print(0)
    elif cal[0] == "toggle" :
        if cal[1] in s : s.discard(cal[1])
        else : s.add(cal[1])
    elif cal[0] == "all" : s= {i for i in range(1,21)}
    elif cal[0] == "empty" : s = set()
