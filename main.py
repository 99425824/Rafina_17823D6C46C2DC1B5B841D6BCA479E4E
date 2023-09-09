# 1.1 Implement a recursive function to calculate the fractional of a given number.


def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n - 1)


number = int(input("Enter a value:"))

res = fact(number)
print("The factorial of {} is {}.".format(number, res))
 