#Equations of motions

print('Operations on basic kinematic equations')

print('For time, type t')
print('For distance, type s')
print('For acceleration, type a')
print('For initial velocity, type u')
print('For final velocity, type v')

n = input('Type the unknown value: ')

if n == 's':
    t = float(input('Enter the value of time: '))
    u = float(input('Enter the value of initial velocity: '))
    v = float(input('Enter the value of final velocity: '))
    a = float(input('Enter the value of acceleration: '))

    s = u*t + (a*(t**2))/2

    print('The distance is ' + str(s))

elif n == 't':
    u = float(input('Enter the value of initial velocity: '))
    v = float(input('Enter the value of final velocity: '))
    a = float(input('Enter the value of acceleration: '))

    t = (v - u)/a

    print('The time is' + str(t))

elif n == 'a':
    u = float(input('Enter the value of initial velocity: '))
    v = float(input('Enter the value of final velocity: '))
    t = float(input('Enter the value of time: '))

    a = (v - u)/t

    print('The acceleration is ' + str(a))

elif n == 'v':
    u = float(input('Enter the value of initial velocity: '))
    a = float(input('Enter the value of acceleration: '))
    t = float(input('Enter the value of time: '))

    v = u + a*t

    print('The final velocity is ' + str(v))

elif n == 'u':

    v = float(input('Enter the value of final velocity: '))
    a = float(input('Enter the value of acceleration: '))
    t = float(input('Enter the value of time: '))

    u = v - a*t

    print('The initial velocity is ' + str(u))

else:
    print('Error: Input unknown')
    break
