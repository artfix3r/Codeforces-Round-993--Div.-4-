#https://codeforces.com/contest/2044/problem/B
n=int(input())
 
while n!=0:
    s=input()
    s1=s[::-1]
    s2=""
    for i in range(0,len(s1)):
        if(s1[i]=='q'):
            s2=s2+'p'
        elif (s1[i]=='p'):
            s2=s2+'q'
        else:
            s2=s2+'w'
    print(s2)
    n-=1