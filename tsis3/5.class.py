class Bank:
    def __init__(self,owner,balance):
        self.o=owner
        self.b=balance
    def deposit(self):
        dep=int(input())
        self.b+=dep
        
    def withdraw(self):
        w=int(input())
        if w>self.b:
            print("eror")
        else:
            self.b-=w
ow=str(input())
ba=int(input())            
p=Bank(ow,ba)
p.deposit()
print(p.b)
p.withdraw()
print(p.b)
    