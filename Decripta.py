import sys
import base64
from typing import List
from text_chunk import TextChunk, block_size

def decrypt_rsa(encrypted_text: str, key: int, module) -> str:
    decrypted_text = ""
    encrypted_chunks = encrypted_text.strip().split('\n')

    for chunk in encrypted_chunks:
        encrypted_chunk = int(chunk)
        decrypted_chunk = pow(encrypted_chunk, key, module)
        decrypted_text += str(TextChunk(decrypted_chunk))

    decrypted_text = base64.b64decode(bytes(decrypted_text,"utf-8")).decode('utf-8', "ignore")
    return decrypted_text

def read_key_file(filename: str) -> int:
    with open(filename, 'r') as file:
        key_data = file.read().split('\n')
        n = int(key_data[0])
        d = int(key_data[1])
    return n, d

def read_data_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def write_output_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def main(argv: List[str]) -> None:
    if len(argv) != 3:
        print("Usage: python decripta.py private_key.txt encrypt_texto.txt decrypted_texto.txt")
        return
    
    key_file = argv[0]
    input_file = argv[1]
    output_file = argv[2]
    
    n, d = read_key_file(key_file)
    encrypted_data = read_data_file(input_file)
    decrypted_data = decrypt_rsa(encrypted_data, d, n)
    write_output_file(output_file, decrypted_data)

if __name__ == '__main__':
    main(sys.argv[1:])
