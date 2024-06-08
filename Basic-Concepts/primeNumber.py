def is_prime(number: int) -> bool:
    factors = 0
    for i in range(2, number):
        if (number % i) == 0:
            factors = factors + 1
    if factors == 0:
        print("prime number")
    else:
        print("Not a prime number")
    
number = 8
is_prime(number)