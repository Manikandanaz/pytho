
class parent:
    def funa(self):
        print('Yes')
class child1:
    def funa1(self):
        print('no')
class child2(parent,child1):
    def funa2(self):
        print('uuu')
s1=child2()
s1.funa()
s1.funa1()
s1.funa2()