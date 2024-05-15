words = []
n = 0

def censorship():
    s = input('Введите слово: ')
    wordsArray = s.split(' ')
    for i in range(len(wordsArray)):
        for j in range(len(words)):
            if wordsArray[i].lower() in words[j].lower():
                a = len(wordsArray[i])
                wordsArray[i] = ''
                for j in range(a):
                    wordsArray[i] += '*'
    print(wordsArray)
    
while int(n) != 4:
    n = input('1. Вывести список запрещенных слов\n2. Проверить их\n3. Пополнить список\n4. Выход\n')
    n = int(n)
    if n == 1:
        if len(words) == 0:
            print('Слов нет.\n')
        else:
            print(words)       
    elif n == 2:
        censorship()
    elif n == 3:
        s = input('Вводите слова через пробел\n')
        words.extend(s.split(' '))