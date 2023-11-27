import gmpy2
import time
import sys
import random

def miller_rabin(n, k=40):
    # Taken from https://gist.github.com/Ayrx/5884790
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n & 1 == 0:
        return False

    r, s = 0, n - 1
    while s & 1 == 0:
        r += 1
        s //= 2
    i = 0
    #while i <= k:
    for _ in range(0,k):
        #print(i,k)
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x in [1, n - 1]:
            continue
        j = 0
        while j <= r - 1:
            x = pow(x, 2, n)
            if x == n - 1:
                break
            j += 1
        else:
            return False
    return True


def _is_prime_fermat(n,b=2):
    """Fermat's prime criterion
  Returns False is returned if x is definitely composite, True if posible prime."""
    i = pow(b,n-1,n)
    return i in [1, 0]


def _is_prime_fermat_gmpy(n,b=2):
  """Fermat's prime criterion
  Returns False is returned if x is definitely composite, True if posible prime."""
  i = gmpy2.powmod(b,n-1,n)
  return i == 1


def _is_prime_mr(n):
    return False if not _is_prime_fermat(n) else miller_rabin(n)

def _is_prime_mr_2(n):
  if _is_prime_fermat(n) and _is_prime_fermat(n,b=3):
    return miller_rabin
  else:
    return False

def _is_prime_mr_3(n):
  if _is_prime_fermat(n) and _is_prime_fermat(n,b=3) and _is_prime_fermat(n,b=5):
    return miller_rabin
  else:
    return False

def _is_prime_mr_4(n):
  if _is_prime_fermat(n) and _is_prime_fermat(n,b=3) and _is_prime_fermat(n,b=5) and _is_prime_fermat(n,b=7):
    return miller_rabin
  else:
    return False

def _is_prime_mr_5(n):
  if _is_prime_fermat(n) and _is_prime_fermat(n,b=3) and _is_prime_fermat(n,b=5)  and _is_prime_fermat(n,b=7) and _is_prime_fermat(n,b=11):
    return miller_rabin
  else:
    return False


def _is_prime_gmpy(n):
    return False if not _is_prime_fermat_gmpy(n) else gmpy2.is_prime(n)


def _is_prime_gmpy_2(n):
  if not _is_prime_fermat_gmpy(n) and _is_prime_fermat_gmpy(n,b=3):
    return False
  else:
    return gmpy2.is_prime(n)



def timeit2(f, l, F=None):
    t0 = time.time()
    for b in range(5, l):
        f(b)
    Fn = F.__name__ if F != None else "None"
    print("%s %s %f" % (f.__name__.ljust(30), Fn.ljust(30), time.time() - t0))


def test(l):
    print("=" * 80)
    print("Iterations: %d" % l)

    timeit2(_is_prime_fermat,l)
    timeit2(_is_prime_fermat_gmpy,l, F=gmpy2.powmod)
  
    print("-" * 80)
 
    timeit2(miller_rabin, l)
    timeit2(_is_prime_mr, l, F=miller_rabin)
    timeit2(_is_prime_mr_2, l, F=miller_rabin)
    timeit2(_is_prime_mr_3, l, F=miller_rabin)
    timeit2(_is_prime_mr_4, l, F=miller_rabin)
    timeit2(_is_prime_mr_5, l, F=miller_rabin)



    print("-" * 80)

    timeit2(gmpy2.is_prime, l)
    timeit2(_is_prime_gmpy , l, F=gmpy2.is_prime)
    timeit2(_is_prime_gmpy_2 , l, F=gmpy2.is_prime)


if __name__ == "__main__":
    test(100000)

