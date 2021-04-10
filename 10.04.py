def lol(name):
    ind = 0
    with open(name + '.txt', encoding='utf-8') as file:
        a = file.read().split('\n')
    while True:
        if ind > len(a) - 1:
            break
        stroka = yield a[ind]
        if stroka == 'next':
            ind += 1
        if stroka == 'prev' and ind >= 1:
            ind -= 1
kek = lol('1')
print(next(kek))
print(kek.send('next'))
print(kek.send('prev'))