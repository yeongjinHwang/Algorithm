import sys
input = sys.stdin.readline

n = int(input())
point = list(map(int, input().split()))

sort_point = sorted(list(set(point)))
dic = {sort_point[i] : i for i in range(len(sort_point))}
for i in point:
    print(dic[i], end = ' ')