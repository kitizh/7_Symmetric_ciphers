import string


def caesar_encrypt(text, key):
    """
    Шифрует текст обобщённым шифром Цезаря.
    """
    alphabet = string.printable  # Используем все печатаемые символы
    encrypted = []
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + key) % len(alphabet)
            encrypted.append(alphabet[new_index])
        else:
            encrypted.append(char)
    return ''.join(encrypted)


def caesar_decrypt(text, key):
    """
    Дешифрует текст, зашифрованный обобщённым шифром Цезаря.
    """
    alphabet = string.printable
    decrypted = []
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) - key) % len(alphabet)
            decrypted.append(alphabet[new_index])
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def test_caesar_cipher():
    # Чтение текста из файла
    input_file = "text.txt"
    encrypted_file = "encrypted_caesar.txt"
    decrypted_file = "decrypted_caesar.txt"
    key = 5

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Шифрование
    encrypted_text = caesar_encrypt(text, key)
    with open(encrypted_file, "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    print(f"Зашифрованный текст записан в файл: {encrypted_file}")

    # Дешифрование
    decrypted_text = caesar_decrypt(encrypted_text, key)
    with open(decrypted_file, "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    print(f"Расшифрованный текст записан в файл: {decrypted_file}")


if __name__ == "__main__":
    test_caesar_cipher()
