def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print('Fact(1)= ',fact(1))
print('Fact(5)= ',fact(5))