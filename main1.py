import math
num = int(input("Enter number to check:"))
res = math.sqrt(num)
if int(res)==math.sqrt(num):
    print("Perfect square")
else:
    print("Not a perfect square")