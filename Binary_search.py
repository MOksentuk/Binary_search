print('Введите длину списка:')
endsp = int(input())
print('Введите элементы списка через пробел (в убывающем порядке):')
sp = list(map(int, input().split(' ')))
print('Введите элемент, индекс которого нужно выяснить:')
el = int(input())
begsp = 0
steps = 0
while True:
    mid = (endsp + begsp) // 2
    if mid == begsp:
        print('Такого элемента в списке нет')
        break
    elif sp[mid] == el:
        steps += 1
        print(mid, steps)
        break
    elif sp[mid] > el:
        steps += 1
        endsp = mid
    elif sp[mid] < el:
        steps += 1
        begsp = mid
