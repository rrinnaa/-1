a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if d < 0:
 print('Корней нет')
elif d == 0:
 print(f'Единственный корень {-b / (2 * a)}')
elif d > 0:
 print(f'Первый корень уравнения {(-b + d ** 0.5) / (2 *
a)}\nВторой корень уравнения: {(-b -d ** 0.5) / (2 * a)}')