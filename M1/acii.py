for i in range(1, 6):
    stars = '*' * i
    print(stars)

print('--------')

for i in range(0, 10):
    if i % 2 == 0:
        stars = '* ' * 10
    else:
        stars = ' *' * 10
    print(stars)

print('--------')

for i in range(0, 4):
    stars = '* ' * (i*2)
    print(stars)
    print(stars)

print('--------')

for i in range(6, 0, -1):
    stars = '* ' * i
    print(stars)
