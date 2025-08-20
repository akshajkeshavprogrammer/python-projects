a=int(input("Enter your number"))
b=int(input("Enter till which number you want the table to go"))
c=b+1
for i in range(1,c,1):
    print(a,"*",i,"=",a*i)
