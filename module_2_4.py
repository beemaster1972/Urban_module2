def _is_prime(value):
    for _ in range(2, int(pow(value,1/2))+1, 1):
        if value % _ == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [el for el in numbers if _is_prime(el) and el !=1]
not_primes = [el for el in numbers if not _is_prime(el) and el != 1]
print('Primes:', primes)
print('Not Primes:',not_primes)