from random import randint

def is_valid(user_number):
    if 1 <= user_number <= 100:
        return True
    else:
        return False
print('Добро пожаловать в числовую угадайку')
n = int(input('Верхняя граница: '))
key = randint(1, n)
attempts = 0
while True:
    attempts += 1
    user_number = int(input('Число: '))
    if is_valid(user_number):
        if user_number == key:
            print('Вы угадали, поздравляем! Попытки: ' + str(attempts))
            if input('Введите exit для выхода \n') == 'exit':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
            else:
                print('Новая игра')
                attempts = 0
                n = int(input('Верхняя граница: '))
                key = randint(1, n)
        elif user_number > key:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif user_number < key:
            print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        pass
