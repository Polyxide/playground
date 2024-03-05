

'100 enumerated flats, 5 entrances, 4 flats on each floor'

def counter(num):
    print(f'entrance is {(num - 1) // 20 + 1}')
    print(f'floor is {(num - 1) % 20 // 4 + 1}')

counter(int(input('Enter your flat ')))



