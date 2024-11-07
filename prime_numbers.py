def find_prime_numbers(limit):
    prime_numbers = []
    for num in range(2, limit + 1):
        count = 0
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            prime_numbers.append(num)
    return prime_numbers
