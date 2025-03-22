class stack:
    def __init__(self):
        self.stk=[]
        self.top=0
    def push(self,data):
        appending=self.stk.append(data)
    def pop(self):
        popping=self.stk.pop()
    

obj=stack()
x="apple"
lst=list(x)
print("The given input for reversing is:",lst)
for i in lst:
    obj.push(i)
    print(obj.stk)
obj.stk=obj.stk[::-1] #revesing  the stack

print("The reversed string is:",obj.stk)