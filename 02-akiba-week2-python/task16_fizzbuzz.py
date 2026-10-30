first=int(input("enter the starting number:"))
last=int(input("enter the last number:"))
for i in range(first,last):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)

