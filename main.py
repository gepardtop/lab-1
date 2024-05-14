words = []
n = 0
while int(n) != 4:
    n = input('1. Вывести список запрещенных слов\n2. Проверить их\n3. Пополнить список\n 4. Выход\n')
    n = int(n)
    if n == 1:
        if len(words) == 0:
            print('Слов нет.\n')
        else:
            print(words)       
    elif n == 2:
        s = input('Введите слово: ')
        for i in range(len(words)):
            if s in words[i]:
                a = len(s)
                s = ''
                for j in range(a):
                    s += '*'
        print(s)
    elif n == 3:
        s = input('Вводите слова через пробел\n')
        words.extend(s.split(' '))

        