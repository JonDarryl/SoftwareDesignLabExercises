def product(m, n):
    if m < n:
        return product(n, m)

    elif n != 0:
        return (m + product(m, n - 1))

    else:
        return 0
m = 6
n = 9
print("The product of two positive integers, m and n, using only addition and subtraction is:")
print(product(m, n))