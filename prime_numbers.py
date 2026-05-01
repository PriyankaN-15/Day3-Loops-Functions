# Prime Numbers up to N

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # optimized
        if num % i == 0:
            return False
    return True

n = int(input("Enter limit: "))

for i in range(1, n + 1):
    if is_prime(i):
        print(i)