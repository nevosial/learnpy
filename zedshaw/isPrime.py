# Check if input is prime.
def isPrime(n = 1):
    if n < 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True

# Generate list of primes numbers till 100
def list_primes():
    for z in range(100):
        if isPrime(z):
            print(z, end=' ')


b = isPrime(6)
print(f"6 is a prime number? {b}")
c = isPrime(7)
print("7 is a prime number ? {}".format(c))
print("List of primes till 100.")
list_primes()
