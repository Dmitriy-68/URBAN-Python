def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        if a % 2 == 0:
            print('Составное')
        else:
            k = 0
            for i in range(3, a // 3 + 1, 2):
                if a % i == 0:
                    k += 1
            if k == 0:
                print('Простое')
            else:
                print('Составное')
        return a

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(28, 7, 32)
print(result)
