n = int(input("Enter the value of n? "))
sum=0
count = 1
while count <= n:
    x = int(input("Enter the %d number? "%(count)))  # In Python both %s and %d are placeholders for a string and a number respectively.
                                          # %s will return the string and %d will return number, the values are passed using % operator.
    sum = sum + x
    count = count + 1
average  = sum / n
print("The Average is ", average)
