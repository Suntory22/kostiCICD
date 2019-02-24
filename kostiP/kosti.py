#!/usr/bin/env python3

# Игра в виртуальные кости
# Версия 1.3

import random, time


def calculate_luck_level(guess, cube1_player, cube2_player, cube3_player, cube4_player):
    return abs(guess - (cube1_player + cube2_player + cube3_player + cube4_player))


def output_luck_level(luck_level):
    luck_levels = ["Ты угадал! Круто!", "Ты был близко", "Не угадал :с"]
    if luck_level == 0:
        return luck_levels[0]
    elif luck_level <= 3:
        return luck_levels[1]
    else:
        return luck_levels[2]


def solo1(guess):
    cube1_player = random.randint(1,6) 
    # print("\nПолетели кости..! Да прибудет со мной удача! ")
    # time.sleep(2)
    # print(f"\nВам выпадает: {cube1_player}") 
    time.sleep(1)
    luck_level = calculate_luck_level(guess, cube1_player, 0, 0, 0)
    print(output_luck_level(luck_level))
    return str(cube1_player),


def solo2(guess):
    cube1_player = random.randint(1,6) 
    cube2_player = random.randint(1,6) 
    # print("\nПолетели кости..! Да прибудет со мной удача! ")
    # time.sleep(2)
    print(f"\nВаш первый кубик: {cube1_player}") 
    time.sleep(1)
    print(f"Ваш второй кубик: {cube2_player}")  
    total_player = cube1_player + cube2_player 
    # time.sleep(1)
    print(f"\nИтого: {total_player}")    
    luck_level = calculate_luck_level(guess, cube1_player, cube2_player, 0, 0)
    print(output_luck_level(luck_level))
    return str(cube1_player), str(cube2_player),


def solo3(guess):
    cube1_player = random.randint(1,6) 
    cube2_player = random.randint(1,6) 
    cube3_player = random.randint(1,6) 
    # print("\nПолетели кости..! Да прибудет со мной удача! ")
    # time.sleep(2)
    print(f"\nВаш первый кубик: {cube1_player}") 
    time.sleep(1)
    print(f"Ваш второй кубик: {cube2_player}")  
    # time.sleep(1)
    print(f"Ваш третий кубик: {cube3_player}") 
    total_player = cube1_player + cube2_player + cube3_player
    # time.sleep(1)
    # print(f"\nИтого: {total_player}")    
    luck_level = calculate_luck_level(guess, cube1_player, cube2_player, cube3_player, 0)
    print(output_luck_level(luck_level))
    return str(cube1_player), str(cube2_player), str(cube3_player),


def solo4(guess):
    cube1_player = random.randint(1,6) 
    cube2_player = random.randint(1,6) 
    cube3_player = random.randint(1,6) 
    cube4_player = random.randint(1,6) 
    # print("\nПолетели кости..! Да прибудет со мной удача! ")
    # time.sleep(2)
    print(f"\nВаш первый кубик: {cube1_player}") 
    time.sleep(1)
    print(f"Ваш второй кубик: {cube2_player}")  
    # time.sleep(1)
    print(f"Ваш третий кубик: {cube3_player}") 
    # time.sleep(1)
    print(f"Ваш четвертый кубик: {cube4_player}") 
    total_player = cube1_player + cube2_player + cube3_player + cube4_player
    # time.sleep(1)
    # print(f"\nИтого: {total_player}")    
    luck_level = calculate_luck_level(guess, cube1_player, cube2_player, cube3_player, cube4_player)
    print(output_luck_level(luck_level))
    return str(cube1_player), str(cube2_player), str(cube3_player), str(cube4_player),


# Узнаем в какой режим желает играть пользователь
def ver():                   
    answer = input("\nВыберите количество игральных костей от 1 до 4. \nДля выхода введите \"X\" \nВаш выбор: ")
    if answer == "1":
        guess = int(input("\nВаша ставка: "))
        solo1(guess) 
        exit()
    if answer == "2":
        guess = int(input("\nВаша ставка: "))
        solo2(guess) 
        exit()
    if answer == "3":
        guess = int(input("\nВаша ставка: "))
        solo3(guess) 
        exit()
    if answer == "4":
        guess = int(input("\nВаша ставка: "))
        solo4(guess) 
        exit()
    elif answer.upper() == "X":
        exit() 
    else: 
        print("\nНе шути со мной, выбирай правильно! >:(") 
        ver() 


if __name__ == '__main__':
    global player
    print("Добро пожаловать в игру \"ВИРТУАЛЬНЫЕ КОСТИ\"")
    print("Версия: 1.3")
    ver()
