test = str(input("enter a word to test "))

reverse = test[::-1]

if test == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


