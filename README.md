A simple script to measure isprime timings

=== Python 3.9 ===
```
================================================================================
Iterations: 100000
_is_prime_fermat               None                           0.305681
_is_prime_fermat_gmpy          powmod                         0.179405
--------------------------------------------------------------------------------
miller_rabin                   None                           2.803342
_is_prime_mr                   miller_rabin                   2.093703
_is_prime_mr_2                 miller_rabin                   0.205150
_is_prime_mr_3                 miller_rabin                   0.222880
_is_prime_mr_4                 miller_rabin                   0.240087
_is_prime_mr_5                 miller_rabin                   0.261430
--------------------------------------------------------------------------------
is_prime                       None                           0.025881
_is_prime_gmpy                 is_prime                       0.123901
_is_prime_gmpy_2               is_prime                       0.264785
```
=== python 2.7 ===
```
================================================================================
Iterations: 100000
_is_prime_fermat               None                           0.168082
_is_prime_fermat_gmpy          powmod                         0.177032
--------------------------------------------------------------------------------
miller_rabin                   None                           1.691520
_is_prime_mr                   miller_rabin                   1.591365
_is_prime_mr_2                 miller_rabin                   0.201280
_is_prime_mr_3                 miller_rabin                   0.217201
_is_prime_mr_4                 miller_rabin                   0.230551
_is_prime_mr_5                 miller_rabin                   0.231607
--------------------------------------------------------------------------------
is_prime                       None                           0.041019
_is_prime_gmpy                 is_prime                       0.216889
_is_prime_gmpy_2               is_prime                       0.426251

```
