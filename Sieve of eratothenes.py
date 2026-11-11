def sieve_of_eratosthenes(n):
  primes = [True] * (n + 1)
  primes[0] = primes[1] = False
  for p in range(2, int(n**0.5) + 1):
    if primes[p]:
      # Mark multiples of p starting from p^2 as non-prime
      for i in range(p * p, n + 1, p):
        primes[i] = False
  return [i for i, is_prime in enumerate(primes) if is_prime]