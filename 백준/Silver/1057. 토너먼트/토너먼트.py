import sys
input = sys.stdin.readline

n,a,b = list(map(int,input().split()))
cnt=0
while a!=b :
    a -= a//2
    b -= b//2
    cnt+=1
print(cnt)