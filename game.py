import random

print('Добро пожаловать в числовую угадайку')

#возвращает результат проверки валидности
def is_valid(text, k, l):
    return text.isdigit() and k <= int(text) <= l

#возвращает значения диапазона чисел и рандомное число
def start_game():
    print('Введите два целых числа')
    m, n = int(input()), int(input())
    m = min(m, n)
    n = max(m, n)
    num = random.randint(m, n)
    return m, n, num
     

#продолжить игру или нет
def continue_game():
    s = input()
    if s.lower() == 'y':
        game()
    else:
        print('Спасибо, что сыграли в угадайку 😊')
        return False

#угадываем число
def game():
    count = 0

    #вернули числа
    m, n, num = start_game()
    print('Попробуйте угадать число')

    #запускаем цикл
    while True:
        guess = input()

    #проверка валидности
        if not is_valid(guess, m, n):                           
            print('А может быть все-таки введем целое число от', m, 'до', n, '?')
            count += 1
            continue
        else:
            guess = int(guess)                 

        #проверяем угаданное число   
        if guess > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        elif guess < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('Вы угадали, поздравляем!')
            print('Попыток предпринято :', count)

        #возможность сыграть заново
            print('Хотите продолжить? Y или N')                  
            result = continue_game()
            if not result:
                break

game()