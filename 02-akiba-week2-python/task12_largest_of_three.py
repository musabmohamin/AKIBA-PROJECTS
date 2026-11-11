x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if x==y and x==z:
    print("All three numbers are equal")
elif x>y and x>z:
    print("The largest number is:",x)
    if x==y or x==z: 
        print("The largest number is equal to one of the other numbers",x)
elif y>z:
    print("The largest number is:",y)
    if y==z:
        print("The largest number is equal to one of the other numbers",y)
else:
    print("The largest number is:",z)