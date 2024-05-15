# Групп. динам

# Программа антицензуры
```
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
```
# Условие задачи 
Для расширения функциональности системы автоцензуры необходимо
приложение, которое заменяет любое слово из некоторого множества
(множество задает пользователь) на символы ****, где количество
символов соответствует количеству символов в исходном слове.

# Скриншоты
![image](https://github.com/gepardtop/lab-1/assets/85400129/9c1e16c3-1642-4ed7-9328-838146025592)
![image](https://github.com/gepardtop/lab-1/assets/85400129/564bc4df-5052-47a8-a87e-5821442e3d6b)


