import sys
import json
from typing import List
from text_chunk import TextChunk, block_size

def decrypt_rsa(encrypted_data: str, key: int) -> str:
    decrypted_text = ""
    encrypted_blocks = encrypted_data.strip().split('\n')

    for encrypted_block in encrypted_blocks:
        encrypted_chunk = int(encrypted_block)
        decrypted_chunk = pow(encrypted_chunk, key, key)
        decrypted_text += str(decrypted_chunk)

    return decrypted_text

def read_key_file(filename: str) -> int:
    with open(filename, 'r') as file:
        key_data = json.load(file)
    return key_data['n']

def read_data_file(filename: str) -> str:
    with open(filename, 'r') as file:
        data = file.read()
    return data

def write_output_file(filename: str, data: str) -> None:
    with open(filename, 'w') as file:
        file.write(data)

def main(argv: List[str]) -> None:
    if len(argv) != 3:
        print("Usage: python decripta.py private_key.txt encrypted_texto.txt decrypted_texto.txt")
        return
    
    key_file = argv[0]
    input_file = argv[1]
    output_file = argv[2]
    
    key = read_key_file(key_file)
    encrypted_data = read_data_file(input_file)
    decrypted_data = decrypt_rsa(encrypted_data, key)
    write_output_file(output_file, decrypted_data)

if __name__ == '__main__':
    main(sys.argv[1:])
