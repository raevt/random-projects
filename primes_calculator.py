"""
    Rae Adimer
    Calculates primes between two numbers
    Yes this is super inefficient
"""
import math

def gen_not_primes(maximum, minimum):
    not_primes = set()
    starting_point = math.ceil(minimum**(1/2))
    if starting_point < 2:
        starting_point = 2
    for i in range(starting_point, maximum + 1):
        for n in range(2, maximum + 1):
            if (i * n) <= maximum and (i * n) >= minimum and (i * n) not in not_primes:
                not_primes.add(i * n)
    return sorted(not_primes)

def gen_primes(not_primes, minimum, maximum):
    primes = []
    if minimum < 2:
        minimum = 2
    for i in range(minimum, maximum + 1):
        if i not in not_primes:
            primes.append(i)
    return primes

def main():
    minimum = int(input("Enter the minimum value:"))
    maximum = int(input("Enter the maximum value:"))
    print(gen_primes(gen_not_primes(maximum, minimum), minimum, maximum))

if __name__ == "__main__":
    main()