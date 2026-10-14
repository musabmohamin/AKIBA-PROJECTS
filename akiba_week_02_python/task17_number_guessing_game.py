secret_number=5
count=0
while count<5:
    number=int(input("Enter a number 1 upto 20:"))
    count=count+1
    
    if number==secret_number:
        print(f"CONGRATULATION! you guessed the number in {count} attempt ")
        break
            
print("GAME OVER! you have used all your attempts")
