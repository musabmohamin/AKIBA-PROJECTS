word=input("Enter a word:")
word=word.lower()
word_backward=word[::-1]
if word==word_backward:
    print("The word you entered is a palindrome")
else:
    print("The word you entered is not a palindrome")    