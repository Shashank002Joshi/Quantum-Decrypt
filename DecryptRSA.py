import numpy as np
from math import sqrt,log,gcd
import random
from random import randint
import rsa

def decrypt(ciphertext, package):
    d, n = package
    plaintext = [chr(pow(c, d, n)) for c in ciphertext]
    return (''.join(plaintext))

def drsa(cb,pk):
    return decrypt(cb ,pk)