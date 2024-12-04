import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
sort_p = sorted(p)

time = 0
person = len(sort_p)-1
for i in sort_p :
    time += i*person +i
    person-=1
print(time)
