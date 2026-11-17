numbers=[2, 7, 11, 15]
target=9
right=len(numbers)-1
left=0
while left<right:
    if numbers[left]+numbers[right]==target:
        print([left,right])
        break
    elif numbers[left]+numbers[right]<target:
        left+=1
    else:
        right-=1