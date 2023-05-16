class class1:
    def __init__(self) -> None:
        self.env='dev'
    def update(self):
        self.db='fdl'
        print('the environement is',self.env)
    def ky(self):
        print('i am from ky',self.env,self.db)
obj=class1()
obj.update()
obj.ky()