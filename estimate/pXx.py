

N = int(input())
n = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))
answer = [0]*M
n.sort()


for i in range(M):
    x = m[i]
    left = 0
    right = N-1
    while(left<=right):
        mid = (left+right)//2
        ga=0
        if(n[mid]==x):
            answer[i]=1
            break
        elif(n[mid]<x):
            left = mid+1
        else:
            right = mid-1


        # -10 2 3 6 10
    
    
    
print(' '.join(map(str, answer)))
