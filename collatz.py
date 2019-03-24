#Kiyoko Saito 2019-3-21
# This is solution for Q4 

start = int(input("Please enter an integer: "))
ans = 1

while ans !=1:
  if ans % 2 == 0:
    ans = ans//2
    
  
else:
    ans = ans * 3 + 1
    

print (list(ans(start)))