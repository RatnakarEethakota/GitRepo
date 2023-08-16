# Python program to check if difference between sum of
# odd digits and sum of even digits is 0 or not

# Reading Input
num = int(input())
string1 = str(num)
evensum = 0
oddsum = 0

# Driver Code
for i in range(0, len(string1)):
    if (i % 2 == 0):
        evensum += int(string1[i])
    else:
        oddsum += int(string1[i])

# Condition
if (oddsum - evensum == 0):
    print("Yes")
else:
    print("No")

print("ok")

num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")