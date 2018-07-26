#5.Design a code which will find the given number
# is Palindrome number or not.
while 1:
    text=str(input("Enter your word : "))
    reverse=text[::-1]

    if(text == reverse):
        print("Its a palindrome")
        break
    else:
        print("Its not a palindrome")
