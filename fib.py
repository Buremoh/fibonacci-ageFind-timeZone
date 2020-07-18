import logging
logging.basicConfig(level=logging.DEBUG)

# Printing the sum of even numbers between 10 and 200 in fibonacci series

# generate fibonacci numbers
fibNumbers = [10, 11]

while fibNumbers[-1] < 200:
    fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

del fibNumbers[-1]
logging.debug(fibNumbers)
# Find all the even numbers
totalSum = 0
evenFibNumbers = []
for fibNumber in fibNumbers:
    if fibNumber % 2 == 0:
        evenFibNumbers.append(fibNumber)
        totalSum += fibNumber

# getting the sum of the even numbers
logging.debug(evenFibNumbers)
print(totalSum)
