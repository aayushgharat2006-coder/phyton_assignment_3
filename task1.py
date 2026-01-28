# finding factorial using while loop
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} is: {fact}")

# finding factorial using for loop
# n = int(input("Enter a number: "))
#
# fact = 1
# i = 1
#
# for i in range(1,n +1):
#     fact *= i
# print(f"Factorial of {n} is: {fact}")