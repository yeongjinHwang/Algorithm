import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sort_a = sorted(a)

result=0
for i in sort_a :
    result += i*max(b)
    b.pop(b.index(max(b)))

print(result)