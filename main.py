def is_palindrome(num):
    if num[::-1]==num:
        return True
    else:
        return False
n = input("Enter number to check:")
if(is_palindrome(n)):
    print("Palindrome")
else:
    print("Not a Palindrome")