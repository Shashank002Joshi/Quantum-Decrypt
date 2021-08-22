
# Quantum Decrypt

Shor’s algorithm is famous for factoring integers in polynomial time. Since the best-known classical algorithm requires superpolynomial time to factor the product of two primes, the widely used cryptosystem, RSA, relies on factoring being impossible for large enough integers.

## RSA ENCRYPTION

RSA encryption, which is used to encrypt everything from files on our hard drives to confidential Internet traffic, is built on the principles of public key exchange and the computationally difficult problem of prime factorization.

For a classical computer, an efficient algorithm for finding the prime factors of a composite number does not exist, meaning that the best we can do is find an answer a little less awful than exponential time. RSA encryption is usually qualified with a bit length, such as 128-bit, 256-bit, etc., which represents the bit length of the key used to encrypt and decrypt data. So a brute-force algorithm with exponential time complexity working on a 128-bit encryption key would need to attempt 2<sup>128</sup> values at a minimum.

This is equal to 340,282,366,920,938,463,463,374,607,431,768,211,456 possible keys and RSA encryption keys haven't been as small as 128-bit in more than a decade. The current standard recommended key length for an RSA encryption key is 2048-bit, which is equal to (340,282,366,920,938,463,463,374,607,431,768,211,456)<sup>16</sup> possible keys.


Like any other key exchange system, RSA encryption uses a public key and a private key to encrypt and decrypt data, except RSA encryption uses two numbers as its public key, a public exponent to use for encrypting a message and a modulus for the encrypting operation that produces the cipher. What makes this modulus so important is the fact that it is the product of two very large prime numbers and knowing those two numbers will allow you to reverse engineer the private key that unlocks the encryption.
## How Shor Algorithm Break RSA Encryption

Shor’s Algorithm is a three-part answer to the problem of prime factorization for any integer, so it works no matter how large the integer involved. The first part is performed on a classical computer in polynomial time, but it is only the set-up for the second and most important part. The second part requires the use of specially constructed quantum circuits to perform the quantum computation needed to find the value you need for the third part, which allows you to find the prime factors of the integer on a classical computer.

The first part of the algorithm is transforming the problem of prime factorization into an equivalent problem that is solvable, namely, finding the period of a modular operation. If you can find the period of this function using as the integer you want to factor as a modulus, you can find the prime factors fairly quickly on a classical computer with some additional calculations.

The problem is that, like prime factorization, finding the period of this modular operation isn’t something a classical computer can do in polynomial time, but Shor showed in the second part of the algorithm that using a theoretical quantum computer your could calculate this period and, most importantly, he was able to prove mathematically that this part of the quantum algorithm ran in polynomial time. After finding the period, a classical computer could use it to find the prime factors of any integer.

  
## Acknowledgements

 - [IBM Qiskit Documentation](https://qiskit.org/textbook)
 
  