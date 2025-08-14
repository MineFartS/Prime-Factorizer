from philh_myftp.biz import *

log = lambda p1, p2, factor: pc.print(
    p1, '*', p2, '=', factor,
    overwrite = True
)

class db:
    primes = array.new(
        file.json('primes.json', [2])
    )
    factors = json.new(
        file.json('factors.json', {})
    )

def GeneratePrimes(n):
    
    largest = db.primes.max()
    if n > largest:

        pc.print('---------')

        primes = []        
        for x in range(largest+1, n+1):
            if num.is_prime(x):
                pc.print(x, overwrite=True)
                primes += [x]
        
        db.primes += primes
        db.primes.rm_duplicates()
        db.primes.sort()

def PrimeFactorizer(semiprime:int):
    
    GeneratePrimes(semiprime)

    factors = {}
    primes = db.primes.filtered(lambda x: (x <= semiprime/2)).shuffled().read()
    pc.print('---------')

    saved = db.factors[semiprime]
    if saved:
        p1, p2 = saved
        log(p1, p2, semiprime)
        return p1, p2

    for p1 in primes:
        for p2 in primes:
                
            factor = p1 * p2

            factors[factor] = [p1, p2]

            log(p1, p2, factor)

            if factor == semiprime:
                
                db.factors += factors

                return p1, p2

