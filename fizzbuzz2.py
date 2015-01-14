import sys

n = 0


i = 1

if len(sys.argv) > 1:
  try:
    n = int(sys.argv[1])
  except ValueError: 
    n = int(raw_input("Oops, that's not a number. Please enter a number. "))
   
else:
  try:
    user_input = raw_input("Please enter a number: ")
    n = int(user_input)
  except ValueError:
    n = int(raw_input("Oops, that's not a number. Please enter a number. "))
  
print "Fizzbuzz counting up to %d" %n

while i <= n:
  if i % 3 == 0 and i % 5 == 0:
    print "fizzbuzz"
  elif i % 3 == 0:
    print "fizz"
  elif i % 5 == 0:
    print "buzz"
  else:
    print i
  i += 1