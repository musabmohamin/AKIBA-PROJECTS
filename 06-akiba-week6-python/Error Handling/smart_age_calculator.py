
try:
    age=(int(input("Enter your age:")))
    if age<0:
        raise ValueError("negative age error")
        
except ValueError as e:
    print("error:",e)
else:
    print("age:",age)