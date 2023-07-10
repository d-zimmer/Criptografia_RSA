import json
import random
import math


def get_keys():
    with open('primeList.txt', 'r') as file:
        primes = file.read().split('\n')

    def get_prime(primes):
        random_index = random.randint(0, len(primes) - 1)
        prime_str = primes[random_index]
        return int(prime_str)

    def calculate_totient(p, q):
        p_minus_one = p - 1
        q_minus_one = q - 1
        return p_minus_one * q_minus_one

    def calculate_e(totient):
        e = 2
        while e < totient:
            if math.gcd(totient, e) == 1:
                break
            e += 1
        return e

    def calculate_d(e, totient):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        _, d, _ = extended_gcd(e, totient)
        return d % totient

    def save_key_to_file(key, file_name):
        key_string = json.dumps(key)
        with open(file_name, 'w') as file:
            file.write(key_string)

    p = get_prime(primes)
    q = get_prime(primes)
    n = p * q
    totient = calculate_totient(p, q)
    e = calculate_e(totient)
    d = calculate_d(e, totient)

    public_key = {"e": e, "n": n}
    private_key = {"d": d, "n": n}

    save_key_to_file(public_key, 'public_key.txt')
    save_key_to_file(private_key, 'private_key.txt')


get_keys()
