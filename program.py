def caesar_encrypt(text):
    shift = 3
    encrypted_text = ""
    for char in text:
        if char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_text = encrypted_text + new_char
        elif char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_text = encrypted_text + new_char
        else:
            encrypted_text += char
    return encrypted_text

message = input("Enter text to encrypt: ")
result = caesar_encrypt(message)
print("Encrypted text:", result)
