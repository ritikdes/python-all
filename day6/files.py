with open("notes.txt", "w") as f:
    print("Enter 5 lines of text")
    for i in range(5):
        line = input(f"line {i+1}: ")
        f.write(line + "\n")

try:
    with open("notes.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File was not found.")

lines = words = chars = 0
try:
    with open("notes.txt", "r") as f:
        for x in f:
            lines += 1
            words += len(x.split())
            chars += len(x.strip())

except FileNotFoundError as e:
    print("File not found error:",e)


print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")