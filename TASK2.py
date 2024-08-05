print("1.add,2.sub,3.mul,4.div")
a=int(input("enter a number"))
b=int(input("enter a number"))
n=int(input("enter no u choose"))
if(n==1):
    print("add")
    c=a+b
    print(c)
elif(n==2):
    print("sub")
    c=a-b
    print(c)
elif(n==3):
    print("mul")
    c=a*b
    print(c)
elif(n==4):
    print("div")
    c=a/b
    print(c)
else:
    print("enter a valid choice")
    
    
    
