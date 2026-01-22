from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os
import hashlib

BS = AES.block_size


def pad(data):
    padding_len = BS - len(data) % BS
    return data + bytes([padding_len]) * padding_len


def unpad(data):
    padding_len = data[-1]
    if padding_len < 1 or padding_len > BS:
        raise ValueError("Invalid padding")
    return data[:-padding_len]


def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1000000)


def encrypt_file(input_path, output_path, password):
    with open(input_path, 'rb') as f:
        data = f.read()
    salt = get_random_bytes(16)
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data))
    with open(output_path, 'wb') as f:
        f.write(salt + cipher.iv + ct_bytes)


def decrypt_file(input_path, output_path, password, return_data=False):
    with open(input_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        ct = f.read()
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        pt = unpad(cipher.decrypt(ct))
    except Exception:
        raise ValueError("MAC check failed. Incorrect password or corrupted file.")

    if return_data:
        return pt.decode(errors='ignore')
    else:
        with open(output_path, 'wb') as f:
            f.write(pt)


def overwrite_encrypted_file(file_path, updated_data, password):
    temp_path = file_path + ".tmp"
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(updated_data)
    encrypt_file(temp_path, file_path, password)
    os.remove(temp_path)
