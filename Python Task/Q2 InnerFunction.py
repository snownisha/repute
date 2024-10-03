def outerFunction(a,b):
    def innerFunction():
        c = a +b
        return c
    return innerFunction()+3
    
addition = outerFunction(5,3)
print(addition)