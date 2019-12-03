def prime(n):
    prime_numbers = []
    stop = int(input(""))
    for i in range(2, stop + 1):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            prime_numbers.append(i)
    print(prime_numbers)
    return prime_numbers[n - 1]
print(prime(4))
print(prime(6))