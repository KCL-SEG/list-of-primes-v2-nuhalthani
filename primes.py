"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if (number_of_primes <= 0):
        raise ValueError("The Value Must Be Greater Than 0.")

    else:
        temp = 2
        count = 0

        while count < number_of_primes:

            isPrime = True

            for i in range (2, temp):
                if temp % i == 0:
                    isPrime = False

            if isPrime:
                list.append(num)
                count += 1

            temp += 1

    return list
