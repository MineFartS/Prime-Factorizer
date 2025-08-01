from __init__ import *

max_prime = 200

wait_time = 3

GeneratePrimes(max_prime)

while True:

    primes = db.primes.filtered(lambda x: x <= max_prime)    
    p1, p2 = primes.random(2)
    
    factor = p1 * p2

    print(p1, '*', p2, '=', factor)
 
    PrimeFactorizer(factor)

    pc.wait(wait_time, False)
    pc.cls()