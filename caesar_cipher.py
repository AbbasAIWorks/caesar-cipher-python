def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # Handle decryption by reversing shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Keep spaces, numbers, symbols unchanged
            result += char

    return result


def main():
    print("=== Caesar Cipher Tool ===")
    
    text = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g. 3): "))
    except ValueError:
        print("❌ Shift must be a number!")
        return

    choice = input("Type 'e' for Encrypt or 'd' for Decrypt: ").lower()

    if choice == 'e':
        output = caesar_cipher(text, shift, "encrypt")
        print("🔐 Encrypted Text:", output)
    elif choice == 'd':
        output = caesar_cipher(text, shift, "decrypt")
        print("🔓 Decrypted Text:", output)
    else:
        print("❌ Invalid choice!")


if __name__ == "__main__":
    main()