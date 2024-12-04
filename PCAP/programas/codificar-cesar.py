text = input("Ingresa un mensaje: ")
cipher = ''

while True:
    num = int(input("Dame el desplazamiento: "))
    if 0 < num < 26:
        break

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + num
    if code > ord('Z'):
        code -= 26
    cipher += chr(code)

print(cipher)