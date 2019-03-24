#Kiyoko Saito 2019-3-21
# This is solution for Q4 

start = int(input("Please enter an integer: "))
ans = int

while start % 2 == 0:
  ans = ans/2
  
if start % 2 == 1:
  ans = ans * 3 + 1

print(ans)
