import random

def play():
    secret = random.randint(1, 100)
    guess = int(input("Угадай число от 1 до 100: "))
    attempts = 1
    while guess != secret and attempts < 7:
        if guess < secret:
            print("Больше")
        else:
            print("Меньше")
        guess = int(input("Попробуй ещё раз: "))
        attempts += 1
    if guess == secret:
        print(f"Угадал, {attempts} попыток понадобилось")
    else:
        print(f"Ты проиграл, было число {secret}")
again = "да"
while again == "да":
    play()
    again = input("Хочешь сыграть ещё раз? (да/нет): ") 