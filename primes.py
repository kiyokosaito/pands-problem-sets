#this is a solution for Q5

x = int(input("Enter a number: "))

# prime numbers are greater than 1
if x > 1:
   for i in range(2,x):
       if (x % i) == 0:
           print("That is not a prime.")
           break
   else:
       print("That is a prime")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(x,"is not a prime.")