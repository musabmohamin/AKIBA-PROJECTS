number=int(input("Enter a positive number: "))
count_even=0
count_odd=0
sum=0
for i in range(1,number+1): 
    sum=sum+i 
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd + 1

print("The sum of numbers from 1 upto",number,"is",sum)
print("The total numbers of even numbers from 1 upto",number,"is",count_even)
print("The total number of odd numbers from 1 upto",number, "is",count_odd)       

