import hashlib
import os
from hashlib import *
from database import *


def generate_salt():
    return b'12345'

def hash_password_salt(password):
    hashed_password = hashlib.sha256(password.encode() + generate_salt()).hexdigest()
    return hashed_password



