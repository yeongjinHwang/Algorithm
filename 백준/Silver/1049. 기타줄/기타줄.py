import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

set_prices = []
solo_prices = []
for i in range(m) :
    tmp = list(map(int,input().split()))
    set_prices.append(tmp[0])
    solo_prices.append(tmp[1])

min_set = min(set_prices)
min_solo = min(solo_prices)

price = 0
while n > 0:
    if n >= 6:
        if min_solo*6 >= min_set :
            price += min_set
        else :
            price += min_solo*6
        n-=6
    else :
        if min_solo*n >= min_set :
            price += min_set
        else :
            price += min_solo*n
        n-=n

print(price)