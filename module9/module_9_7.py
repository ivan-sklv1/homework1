def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res % 2 == 0:
            print(f'Составное')
            return res
        else:
            print(f'Простое')
            return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    total  = a + b + c
    return total

result = sum_three(2, 3, 6)
print(result)