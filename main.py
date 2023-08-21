import string, os

def encrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            key = key.upper()
            if len(key) < len(message):
                key += key[i % len(key)]
            elif len(key) > len(message):
                key = key[i:len(message)]
            result_index = (string.ascii_uppercase.index(char) + string.ascii_uppercase.index(key[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            key = key.lower()
            if len(key) < len(message):
                key += key[i % len(key)]
            elif len(key) > len(message):
                key = key[i:len(message)]
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
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            key = key.upper()
            if len(key) < len(message):
                key += key[i % len(key)]
            elif len(key) > len(message):
                key = key[i:len(message)]
            result_index = (string.ascii_uppercase.index(char) - string.ascii_uppercase.index(key[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            key = key.lower()
            if len(key) < len(message):
                key += key[i % len(key)]
            elif len(key) > len(message):
                key = key[i:len(message)]
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
        
message = input("Input message: ")
key = input("Key: ")
method = input("Select method: [e/d]: ").lower()
if method == "e":
    key = key.replace(" ", "") if " " in key else key
    encrypt(message, key)
elif method == "d":
    key = key.replace(" ", "") if " " in key else key
    decrypt(message, key)
else:
    print("Unknown method")
