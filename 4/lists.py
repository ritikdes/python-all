# Task 1
numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]

for num in numbers:
    if num > 5:
        print(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smalles = num
print(smallest)


total = 0
for num in numbers:
    total = total + num
print(total)

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(count)


# Task 2
secret = 7
count = 0
while(True):
    n = int(input("Guess a number: "))
    count += 1
    if n > secret:
        print("Too high")
    elif n < secret:
        print("Too low")
    elif n == secret:
        print("Correct")
        break
    
print(f"Attempts: {count}")


# Task 3
for n in range(1,51):
    if n % 3 == 0 and n % 9 != 0:
        print(n)

word = "quit"
guesses = []
while(True):
    guess = input("Enter a random word: ")   
    if guess == word:
        break
    guesses.append(guess)

print(",".join(guesses))