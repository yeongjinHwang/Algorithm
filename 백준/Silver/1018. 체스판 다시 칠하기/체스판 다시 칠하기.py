import sys
input = sys.stdin.readline

n = list(map(int,input().split()))

def search(array,row,col) :
    w_cnt=0
    b_cnt=0
    for i in range(8) :
        for j in range(8) :
            if (i+j)%2 == 0 :
                if array[row+i][col+j] == "W" : w_cnt +=1
            else :
                if array[row+i][col+j] == "B" : b_cnt +=1

    return (min(64-(w_cnt+b_cnt), w_cnt+b_cnt))

chess=[]
for i in range(n[0]) :
    chess.append(list(map(str,input().rstrip())))

result = []
for row_stride in range(n[0]-8+1) :
    for col_stride in range(n[1]-8+1) :
        result.append(search(chess,row_stride,col_stride))
print(min(result))