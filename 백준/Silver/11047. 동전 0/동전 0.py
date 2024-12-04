import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))

prices=[]
for i in range(n) :
    price = int(input())
    if price <= k :
        prices.append(price)
num = 0
while k!=0 :
    if k >= prices[-1] :
        num += (k//prices[-1])
        k = k % prices[-1]
    else :
        prices.pop(-1)
print(num)