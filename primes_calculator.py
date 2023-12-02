"""
    Rae Adimer

    Calculates primes between two numbers, minimum and maximum inclusive. I'm not entirely sure if this works 100% of the time.

    It does this by multiplying together all numbers that could multiply to a number in the given range, creating a set of numbers that are not primes. It then iterates through each number in the provided range, checking whether it is in the set. If not, it is a prime number.

    The key to optimizing this is properly defining the numbers that could multiply to something in the range, and not repeating operations.

    My attempt at this is a sort of two-step approach, with an outer for-loop and nested, inner for-loop. The goal is to use relatively-efficient operations in defining the loop's start and end points to only multiply numbers that could multiply to something in the provided range.

    The inner for-loop is pretty clear to optimize, I think. I limit the starting point to the smallest number which multiplies with i (the outer loop iterable) to the minimum, and the ending point to the smallest number which multiplies with i to the maximum.
    
    The outer for-loop is a bit less clear. I believe the starting point of the rounded-up square root of the minimum is optimal: to get to the minimum, it would need to multiply with itself or greater. And because the inner for-loop sets its starting point at the minimum divided by i, that is what it produces (save for the integer rounding aspect). 
    
    The outer for-loop's ending point is the maximum divided by 2; anything above that would multiply with 2 to be greater than the maximum. I'm relatively certain this isn't optimal.
"""
import math
import time

def gen_not_primes(maximum, minimum):
    not_primes = set()
    fail_counter = 0
    # Starts with the rounded-up square root of the minimum (or 2, if the minimum is less than 2)
    # This, I think, is the smallest number which can multiply with a number from the nested for-loop to something in the provided range.
    starting_point = math.ceil(minimum**(1/2))
    if starting_point < 2:
        starting_point = 2
    for i in range(starting_point, maximum // 2 + 1):
        for n in range(minimum // i, (maximum // i) + 1): # Limits the starting point to the smallest number that multiplies with i to the minimum, and the ending point to the smallest number that multiplies with i to the maximum.
            if (i * n) <= maximum and (i * n) >= minimum and (i * n) not in not_primes:
                not_primes.add(i * n)
            else:
                fail_counter += 1 # Count all multiplications that did not "need" to be run
    print("Not-primes identified: " + str(len(not_primes)))
    print("Fail counter: " + str(fail_counter))
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
    minimum = int(input("Enter the minimum value: "))
    maximum = int(input("Enter the maximum value: "))
    ts = time.time()
    print(gen_primes(gen_not_primes(maximum, minimum), minimum, maximum))
    diff = time.time() - ts
    print("Time to solve: " + str(diff))

if __name__ == "__main__":
    main()
