sum=0
count_odd=0
count_even=0
for i in range (1,11):
    number=int(input("Enter a number:"))
    if i==1:
        largest_number=number
        smallest_number=number
    sum=sum+number
    if number%2==0:
        count_even=count_even+1
    else:
        count_odd+=1
    if number>largest_number:
       largest_number=number
    if number<smallest_number:
        smallest_number=number
average=sum/10
print("The largest number is ", largest_number)
print("The smallest number is",smallest_number)
print("The total sum=" ,sum)
print("average=" ,average)
print("number of even=",count_even)
print("number of odd=", count_odd)