# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n=int(input("Integer: ")) 
factors = []
d = 2
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
        if n > 1:
            factors.append(n)
        else:
            break
print('{} = {}' .format(n,factors))