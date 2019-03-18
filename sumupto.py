#Kiyoko Saito 2019-2-7
# sum up to the integer number input

start = int(input("Please enter an integer: "))
ans = 1
i = 1

while i <= start:
  ans = ans + i
  i = i+1

ans = ans-1

print(ans)

