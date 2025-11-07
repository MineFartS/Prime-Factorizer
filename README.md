# Prime Factorizer

#### I created this is an algoritm to more efficiently calculate the two prime numbers from any semiprime number, aka Prime Factorization.

---

## Features:

- Finding Primes
    - Rules out obvious numbers, such as numbers ending in 0, 2, 4, 5, 6, or 8.
- Prime Factorization
    - It caches all attempts in a json file, and scans the cache before guessing
    - Shuffles all potential primes to improve the speed of calculating larger semiprimes
 
---

<h2>How To Use:</h2>

`pip install git+https://github.com/MineFartS/Prime-Factorizer`

```
from prime_factorizer import *

semiprime = 21
p1, p2 = PrimeFactorizer(semiprime)

```

```
> python -m prime_factorizer run 21
```
