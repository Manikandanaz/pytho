import math
a=int(input('enter 1st number '))
print(a)
sum=0
temp=a
while temp>0:
    digit=temp%10
    sum=sum+(digit*digit*digit)
    temp=temp//10
if(sum==a):
    print('Ys')
else:
    print('no')
