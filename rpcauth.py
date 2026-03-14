#!/usr/bin/env python3
import os, sys, hmac, base64

def generate_salt(length):
    return base64.b64encode(os.urandom(length)).decode('utf-8')[:length]

def generate_password():
    return base64.b64encode(os.urandom(32)).decode('utf-8')

def password_to_hmac(salt, password):
    m = hmac.new(salt.encode('utf-8'), password.encode('utf-8'), 'SHA256')
    return m.hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rpcauth.py <username> [password]")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) == 3 else generate_password()
    salt = generate_salt(16)
    password_hmac = password_to_hmac(salt, password)
    print(f'Add to .env:')
    print(f'RPC_USER={username}')
    print(f'RPC_AUTH={username}:{salt}${password_hmac}')
    print(f'RPC_PASSWORD={password}')

main()