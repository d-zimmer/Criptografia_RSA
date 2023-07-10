import sys
import json
from typing import List
from text_chunk import TextChunk, block_size

def encrypt_rsa(text: str, key: int) -> str:
    encrypted_text = ""
    chunk_size = block_size(key)

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunk_values = [ord(c) for c in chunk]
        encrypted_chunk = [pow(val, key, key) for val in chunk_values]
        encrypted_text += "\n".join(str(val) for val in encrypted_chunk)
        encrypted_text += "\n"

    return encrypted_text.strip()

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
        file.write(data.strip())
        file.write('\n')

def main(argv: List[str]) -> None:
    if len(argv) != 3:
        print("Usage: python Encripta.py .\public_key.txt .\texto.txt encrypt_texto.txt")
        return
    
    key_file = argv[0]
    input_file = argv[1]
    output_file = argv[2]
    
    key = read_key_file(key_file)
    data = read_data_file(input_file)
    encrypted_data = encrypt_rsa(data, key)
    write_output_file(output_file, encrypted_data)

if __name__ == '__main__':
    main(sys.argv[1:])
