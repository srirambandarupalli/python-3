n=int(input())
l=input().split()
l.sort()
sum=0
s=len(l)
while(s>0):
    a=int(l[s-1])
    sum=sum*10+a
    s-=1
print(sum)
