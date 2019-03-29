#this is the solution for Q7
# Kiyoko Saito
# adapted from Week 8 video

num = float(input("Please enter a positive number: "))

rootof = num
estimate = 6.0

while float((estimate * estimate) - rootof) > 0.1 :
  estimate -= ((estimate * estimate ) - rootof) / (2 * estimate)

print (f"The square root of {rootof} is approx. {estimate}.")