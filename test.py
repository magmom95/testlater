def is_prime(num):
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def calculate_prime_number(length):
    prime_list = []

    for i in range(2, 100):
        if(is_prime(i) and (len(prime_list) < length)):
            prime_list.append(i)

    return prime_list


n = int(input('Length? '))
print(calculate_prime_number(n))
