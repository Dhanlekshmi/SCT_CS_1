def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26
            result += chr(base + shifted)
        else:
            result += char 

    return result

def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (number): "))

    if choice == '1':
        encrypted = caesar_cipher(text, shift, 'encrypt')
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher(text, shift, 'decrypt')
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
