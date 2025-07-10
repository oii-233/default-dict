from collections import defaultdict
d=defaultdict(list)
n,m=map(int,input().split())
a=[input()for _ in range(n)]
b=[input()for _ in range(m)]
for j in range(n):
    d[a[j]].append(j+1)
for i in b:
    if i in d:
        print(' '.join (map(str,d[i])))
    else:
        print(-1)



        
