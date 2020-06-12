'''
Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.
By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:

5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1

Only two of these chains start with a prime, their sum is 12.
What is the sum of all primes less than 40000000 which generate a chain of length 25?
'''


from timeit import default_timer as timer
from functools import reduce
from fractions import Fraction

def test_prime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    for i in range(5, int(n ** 0.5)):
        if (n % i == 0) : 
            return False
    return True

    for i in range(5, int(n ** 0.5), 6):
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
    return True  


def phi(n, phi_values):
    if n in phi_values:
        return phi_values[n]
    else:
        if test_prime(n):
            phi_values[n] = n - 1
            return n - 1
        else:
            factors = prime_factors(n)
            val = int(n * reduce((lambda x, y: x * y), factors))
            phi_values[n] = val
            return val


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            hold = Fraction(i-1, i)
            if not hold in factors: factors.append(hold)
    if n > 1:
        hold = Fraction(n-1, n)
        if not hold in factors: factors.append(hold)
    return factors


def primes_sieve(n):
    primes = []
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if (sieve[i]):
            primes.append(i)
            for j in range(i, n+1, i):
                sieve[j] = False
    return primes


def main(max, target):
    times = []
    value = []
    phi_values = {}
    total = 0
    step = 1
    primes = primes_sieve(max)
    times.append(timer())
    print(times[-1])
    for i in primes:
        if i >= step*1000000:
            print(i)
            times.append(timer())
            print(times[-1] - times [-2])
            step += 1
        count = 2
        x = i - 1
        while x > 1:
            x = phi(x, phi_values)
            count += 1
            if count > target:
                break
        if count == target:
            total += i
            value.append(i)
    times.append(timer())
    print("Sum: " + str(total))
    print("Time taken: " + str(times[-1] - times[0]))

if __name__ == "__main__":
    main(40000000, 25)
