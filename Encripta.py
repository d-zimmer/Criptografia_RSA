import sys
import base64
from typing import List
from text_chunk import TextChunk, block_size

def encrypt_rsa(text: str, key: int, module) -> str:
    encrypted_text = ""
    chunk_size = block_size(module)
    encoded_chunk = base64.b64encode(bytes(text, 'utf-8'))
    
    for i in range(0, len(encoded_chunk), chunk_size):
        chunk = encoded_chunk[i:i+chunk_size]    
        text_chunk = TextChunk(chunk.decode('utf-8'))
        encrypted_chunk = pow(text_chunk.int_value(), key, module)
        encrypted_text += str(encrypted_chunk) + "\n"

    return encrypted_text.strip()

def read_key_file(filename: str) -> int:
    with open(filename, 'r') as file:
        key_data = file.readlines()
        n = int(key_data[0].strip())
        e = int(key_data[1].strip())
    return n, e

def read_data_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def write_output_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def main(argv: List[str]) -> None:
    if len(argv) != 3:
        print("Usage: python encripta.py public_key.txt texto.txt encrypt_texto")
        return
    
    key_file = argv[0]
    input_file = argv[1]
    output_file = argv[2]
    
    module, key = read_key_file(key_file)
    data = read_data_file(input_file)
    encrypted_data = encrypt_rsa(data, key, module)
    write_output_file(output_file + ".txt", encrypted_data)

if __name__ == '__main__':
    main(sys.argv[1:])
