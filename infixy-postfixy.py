class Stack:
    def __init__(self):
        self.Stc = []    
    def push(self, item):
        self.Stc.append(item)    
    def pop(self):
        return self.Stc.pop()
    def isEmpty(self):
        return (self.Stc == [])
    def peek(self):
        return self.Stc[-1]
    def __str__(self):
        return str(self.Stc)
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    print("the input is:",tokenList)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]): 
                postfixList.append(opStack.pop())
            opStack.push(token)
            '''This loop checks two conditions:
The operator stack (opStack) is not empty.
The operator at the top of the stack (obtained via opStack.peek()) 
has higher or equal precedence compared to the current operator (token) in the infix expression.'''
    
    while not opStack.isEmpty(): #here  we pop all the operators from the stack and append them to the postfix list

        postfixList.append(opStack.pop())
    
    return " ".join(postfixList)

print(infixToPostfix("A + B * C + D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))



