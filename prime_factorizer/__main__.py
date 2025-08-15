from __init__ import *

m = args[0].lower()

if m == 'test':

    if len(args) == 1:
        args[1] = 200

    GeneratePrimes(args[1])

    while True:

        primes = db.primes.filtered(lambda x: (x <= args[1]))
        p1, p2 = primes.random(2)
        
        factor = p1 * p2

        print(p1, '*', p2, '=', factor)
    
        PrimeFactorizer(factor)

        time.sleep(3)
        pc.cls()

elif m == 'run':
    PrimeFactorizer(args[1])

elif m == 'reset':
    db.primes.path.delete()
    db.factors.path.delete()