#!/usr/bin/env python3
"""
Encrypt passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates provided password matches hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
