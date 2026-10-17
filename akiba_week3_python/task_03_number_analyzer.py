
def is_prime(number):
    if number<2:
        return "NOT PRIME"
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return "NO"
        else:
            return "YES"

def get_divisor(number):
    divisors=[]
    for i in range(1,number+1):
        if number%i==0:
            divisors.append(i)
    return divisors

def sum_of_digits(number):
    sum=0
    while number>0:
        digits=number%10
        sum=sum+digits
        number=number//10
    return sum
        
def reverse_number(number):
    reverse=0
    while number>0:
        digits=number%10
        reverse=reverse*10+digits
        number=number//10
    return reverse    
def analyze_number(number):
    if number%2==0:
        return "even"
    else:
        return"odd"


numbers = []

while True:
    number = int(input("Enter a number: "))
    numbers.append(number)

    add = int(input("Enter 1 to add another number or 0 to continue: "))

    if add == 0:
        break

for number in numbers:
    digit_sum = sum_of_digits(number)
    divisor = get_divisor(number)
    prime = is_prime(number)
    reverse = reverse_number(number)
    parity = analyze_number(number)

    print("\n========= SUMMARY OF THE NUMBER =========")
    print("NUMBER:", number)
    print("PRIME:", prime)
    print("DIVISORS:", divisor)
    print("SUM OF DIGITS:", digit_sum)
    print("REVERSE:", reverse)
    print("PARITY:", parity)













