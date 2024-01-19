a = int(input('введите 1 натуральное число:'))
b = int(input('введите 2 натуральное число:'))
c = int(input('введите 3 натуральное число:'))
if a + b > c and c + b > a and c + a > b:
    print('Yes')
else:
    print('No')