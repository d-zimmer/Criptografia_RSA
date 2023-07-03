import random
import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod inverse does not exist")


def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)


def generate_key_pair(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)


def save_key_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(str(key[0]) + '\n')
        file.write(str(key[1]) + '\n')


def load_key_from_file(filename):
    with open(filename, 'r') as file:
        key_lines = file.readlines()
    key = (int(key_lines[0]), int(key_lines[1]))
    return key


def save_encrypted_message_to_file(encrypted_message, filename):
    with open(filename, 'w') as file:
        for num in encrypted_message:
            file.write(str(num) + '\n')


def load_encrypted_message_from_file(filename):
    with open(filename, 'r') as file:
        encrypted_lines = file.readlines()
    encrypted_message = [int(line) for line in encrypted_lines]
    return encrypted_message


def save_decrypted_message_to_file(decrypted_message, filename):
    with open(filename, 'w') as file:
        file.write(decrypted_message)


def main():
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

    public_key, private_key = generate_key_pair(p, q)

    message = input("Digite a mensagem a ser criptografada: ")

    encrypted_message = encrypt(message, public_key)

    save_key_to_file(public_key, 'public_key.txt')
    save_key_to_file(private_key, 'private_key.txt')
    save_encrypted_message_to_file(encrypted_message, 'encrypted_message.txt')

    print("Mensagem original:", message)
    print("Mensagem encriptada:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Mensagem decriptada:", decrypted_message)
    save_decrypted_message_to_file(decrypted_message, 'decrypted_message.txt')

if __name__ == '__main__':
    main()