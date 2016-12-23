import random

N = 10
n_range = 100
print("==== Guess Number =====\n Press any key to start")
random_number = random.randint(0, n_range)
print("Number from %s to %s, guess what!" % (0, n_range))
number = None
while True:
    try:
        user_input = input("Input number: ")
        number = int(user_input)
    except Exception:
        print("Invalid input! It must be a number")
        continue
    delta = abs(number - random_number)
    if number == random_number:
        print("Yaaaaay! Congrats! __You_win__. Buy!")
        break
    if delta == 1:
        print("Hot hot hot! ...")
        continue
    if delta < n_range / 10 + 2:
        print("Very warm...")
        continue
    if delta < n_range / 5 + 3:
        print("Warm...")
        continue
    if delta < n_range / 3:
        print("Mh, not so far...")
        continue
    if delta < n_range / 2:
        print("Cold...")
        continue
    print("Very cold...")
