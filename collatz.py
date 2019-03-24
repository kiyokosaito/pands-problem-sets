start = int(input("Please enter an integer: ")) 
ans = 0

while start % 2 == 0: 
  ans = start//2 

  if start % 2 == 1:
    ans = start * 3 + 1   
   
print (start, ans end =' ')