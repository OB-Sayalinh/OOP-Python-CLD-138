def is_prime(num):
    prime = True
    for x in range(1, (num // 2) + 1):
        if (num / (x) == num // (x)) and x != 1:
            prime = False
            break
    return prime

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
