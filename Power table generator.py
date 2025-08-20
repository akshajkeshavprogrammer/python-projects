a=int(input("Enter your number"))
b=int(input("Enter till which power you want to go"))
c=1

for i in range(1,b+1):
    c=a*c
    print(a," to the power of ",i,"=",c)    

    
