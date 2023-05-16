num=5
prime=True
for i in range(2,num):
    if num%i == 0:
       prime=False
if prime == True:
    print('prime')
else:
    print('not prime')