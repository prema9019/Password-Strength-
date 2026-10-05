text = "Hello, world 2026!"
shift = 4
mode = "encrypt"

if mode == "decrypt":
    shift = -shift

result = ""

for char in text:
    if char.isupper():
        result += chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        result += chr((ord(char) - 97 + shift) % 26 + 97)
    elif char.isdigit():
        result += chr((ord(char) - 48 + shift) % 10 + 48)
    else:
        result += char

print(f"Result ({mode}): {result}")
 