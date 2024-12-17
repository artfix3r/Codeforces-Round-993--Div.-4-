#https://codeforces.com/contest/2044/problem/D
from math import * 
 
def ar() : return list(map(int,input().split()))
 

 
def solve():
    n=int(input())
    a=ar()
 
    done=[0]*(n+1)
    b=[]
    for i in a:
        if done[i]==0:
            b.append(i)
            done[i]=1
    for i in range(1,n+1):
        if(len(b)!=n and done[i]==0):
            b.append(i)
    print(*b)
 
for _ in range(int(input())):
    solve()