x = input().split()

a = float(x[0])
b = float(x[1])
c = float(x[2])

delta = b**2 - 4*a*c

if delta < 0:
    print('Impossivel calcular')

else:
    div = 2*a

    if div == 0:
        print('Impossivel calcular')

    else:
        bhaskara1 = (-b + delta**0.5) / div
        bhaskara2 = (-b - delta**0.5) / div
        
        print('R1 = %.5f' % bhaskara1)
        print('R2 = %.5f' % bhaskara2)