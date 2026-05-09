import random
secret = random.randint(1,100)
count = 0

while(True):
    count += 1
    guess = int(input("Guess a number between 1-100: "))
    distance = secret - guess
    distance = abs(distance)
    if guess == secret:
        print("Congratulation! You won.")
        print(f"You guessed in {count} attempts.")
        break
    else:
        if guess < secret:
            print("Higher")
            if distance <= 10:
                print("Hot! You're close")
            else:
                print("Cold")
        else:
            print("Lower")
            if distance <= 10:
                print("Hot")
            else:
                print("Cold! You are far away")