import os


def vernam_encrypt_decrypt(text, key):
    """
    Шифрует или дешифрует текст с помощью шифра Вернама.
    """
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))


def generate_vernam_key(length):
    """
    Генерирует случайный ключ для шифра Вернама.
    """
    return ''.join(chr(os.urandom(1)[0]) for _ in range(length))


def test_vernam_cipher():
    input_file = "text.txt"
    encrypted_file = "encrypted_vernam.txt"
    decrypted_file = "decrypted_vernam.txt"
    key_file = "vernam_key.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Генерация ключа
    key = generate_vernam_key(len(text))
    with open(key_file, "w", encoding="utf-8") as f:
        f.write(key)
    print(f"Ключ записан в файл: {key_file}")

    # Шифрование
    encrypted_text = vernam_encrypt_decrypt(text, key)
    with open(encrypted_file, "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    print(f"Зашифрованный текст записан в файл: {encrypted_file}")

    # Дешифрование
    decrypted_text = vernam_encrypt_decrypt(encrypted_text, key)
    with open(decrypted_file, "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    print(f"Расшифрованный текст записан в файл: {decrypted_file}")


if __name__ == "__main__":
    test_vernam_cipher()
