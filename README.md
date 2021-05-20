A simple script to measure isprime timings

=== Python 3.9 ===
```
================================================================================
Iterations: 100000
_is_prime_fermat               None                           0.171539
_is_prime_fermat_gmpy          powmod                         0.098606
--------------------------------------------------------------------------------
miller_rabin                   None                           1.803433
_is_prime_mr                   miller_rabin                   1.543666
_is_prime_mr_2                 miller_rabin                   0.216847
--------------------------------------------------------------------------------
is_prime                       None                           0.025171
_is_prime_gmpy                 is_prime                       0.122766
_is_prime_gmpy_2               is_prime                       0.259153
```

=== python 2.7 ===
```
================================================================================
Iterations: 100000
_is_prime_fermat               None                           0.169282
_is_prime_fermat_gmpy          powmod                         0.172265
--------------------------------------------------------------------------------
miller_rabin                   None                           1.699223
_is_prime_mr                   miller_rabin                   1.591952
_is_prime_mr_2                 miller_rabin                   0.213375
--------------------------------------------------------------------------------
is_prime                       None                           0.041959
_is_prime_gmpy                 is_prime                       0.214412
_is_prime_gmpy_2               is_prime                       0.443641
```
