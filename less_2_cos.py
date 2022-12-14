import math
x = float(input("Введіть значення х = "))

if - math.pi <= x <= math.pi:
    y = math.cos(3*x)
    print("y = ", round(y,2))
else:
    print("Значення x не входить до заданого діапазону")
    


