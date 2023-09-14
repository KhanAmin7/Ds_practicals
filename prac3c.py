# Factorial using iteration and recursion
def factorial_re(number):
    if number<0:
        print("cannot find the factorial of negative number")
        return -1
    if number==1 or number==0:
        return 1
    else:
        return number*factorial_re(number-1)
number=int(input("Enter the number\n"))
print("\nfactorial using recursion is",factorial_re(number))

def factorial_iteration(number):
    if number<0:
        print("invalid entry! cannot find the factorial of negative number")
        return -1
    fact=1
    while(number>0):
        fact=fact*number
        number-=1
    return fact
print(f"factorial using iteration is {factorial_iteration(number)}")