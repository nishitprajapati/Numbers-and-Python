#########################################################################################
# get the sum of the digits for a given number
#########################################################################################
k = 552 # can take any integre value
sum = 0
while k > 0:
  sum += k % 10
  k = int(k/10)
print(sum)
########################################################################################
def inspect(x):
  '''this function describes numbers
  whether it is positive or negative
  or zero or none of them'''
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")
 ########################################################################################
