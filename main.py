import string, os

def check_key(message, key):
    new_key = ""
    index = 0
    for char in message:
        if char.isalpha():
            new_key += key[index % len(key)]
            index += 1
        else:
            new_key += char
    return new_key


def encrypt(message, key):
    key = check_key(message, key)
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            key = key.upper()
            result_index = (string.ascii_uppercase.index(char) + string.ascii_uppercase.index(key[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            key = key.lower()
            result_index = (string.ascii_lowercase.index(char) + string.ascii_lowercase.index(key[i])) % 26
            result += string.ascii_lowercase[result_index]
        else:
            result += char

    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == "y":
        os.system("cls")
        with open(f"encrypt.txt", 'w') as f:
            f.write(f"Message: {message}\n")
            f.write(f"Key: {key}\n")
            f.write(f"Result: {result}")
    elif save_file == "n":
        os.system("cls")
        print(f"Message: {message}")
        print(f"Key: {key}")
        print(f"Result: {result}\n")


def decrypt(message, key):
    key = check_key(message, key)
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            key = key.upper()
            result_index = (string.ascii_uppercase.index(char) - string.ascii_uppercase.index(key[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            key = key.lower()
            result_index = (string.ascii_lowercase.index(char) - string.ascii_lowercase.index(key[i])) % 26
            result += string.ascii_lowercase[result_index]
        else:
            result += char

    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == "y":
        os.system("cls")
        with open(f"decrypt.txt", 'w') as f:
            f.write(f"Message: {message}\n")
            f.write(f"Key: {key}\n")
            f.write(f"Result: {result}")
    elif save_file == "n":
        os.system("cls")
        print(f"Message: {message}")
        print(f"Key: {key}")
        print(f"Result: {result}\n")


while True:
    message = input("Input message: ")
    key = input("Alphabet key: ").replace(" ", "")
    if key.isalpha():
        method = input("Select method: [e/d]: ").lower()
        if method == "e":
            encrypt(message, key)
        elif method == "d":
            decrypt(message, key)
        else:
            print("Unknown method\n")
    else:
        print(f"Key '{key}' not alphabet key\n")