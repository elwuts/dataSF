"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np


number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число

    Args:
        number (int, optional): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    
    count = 0
    min = 1
    max = 100
    

    while True:
        count += 1
        mid = round((min + max)/2)
        
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            # print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
        
    return(count)

print(f'Количество попыток: {random_predict(number)}')


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)