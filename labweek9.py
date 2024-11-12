def is_prime(prime_number):
    for x in range(2,(prime_number//2)+1):
        if (prime_number%x) != 0:
            return True
        else:
            return False
    return True
print(is_prime(37))
