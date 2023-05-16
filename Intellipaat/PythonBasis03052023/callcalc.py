# import calc as cc
#a=int(input('enter your first number'))
#b=int(input('enter your second number'))
#C=str(input('enter add/sub/mul/div'))
#if C=='add':
#    cc.add(a,b)
#elif C=='mul':
#    cc.mul(a,b)
#elif C=='div':
#    cc.div(a,b)
#elif C=='sub':
#    cc.sub(a,b)
class A:
    def __init__(self):
        self.name='mani'
        self.age=20
    def details(self):
        print('the name is',self.name)
class B:
    def __init__(self):
        self.name='ragu'
        self.id=1
class c(A,B):
    def __init__(self):
        casl=A()
        casl.details()
        print('this is from classs c ,',casl.name)
    def get_datails(self):
        aclass=A()
        bclass=B()
        print('this is from classs c - aclass,',aclass.name)
        print('this is from classs c - bclass,',bclass.name)
obj=c()
print(obj.get_datails())