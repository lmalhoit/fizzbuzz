n = 30
i = 1
print "Fizzbuzz counting up to 30"

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
  
    


