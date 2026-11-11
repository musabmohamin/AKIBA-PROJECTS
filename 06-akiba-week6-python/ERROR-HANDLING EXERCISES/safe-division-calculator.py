try:
    num1=int(input("enter a number :"))
    num2=(int(input("Enter a second number :")))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("calculation finished")