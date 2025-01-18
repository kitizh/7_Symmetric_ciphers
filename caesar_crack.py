import string
from collections import Counter


def caesar_break(text):
    """
    Восстанавливает текст, зашифрованный обобщённым шифром Цезаря,
    предполагая, что пробел - самый частый символ.
    """
    alphabet = string.printable
    counter = Counter(text)
    most_common_char = counter.most_common(1)[0][0]  # Находим самый частый символ
    space_char = ' '  # Предполагаем, что это пробел
    key = (alphabet.index(most_common_char) - alphabet.index(space_char)) % len(alphabet)

    decrypted = []
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) - key) % len(alphabet)
            decrypted.append(alphabet[new_index])
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def test_caesar_break():
    encrypted_file = "encrypted_caesar.txt"
    broken_file = "broken_caesar.txt"

    with open(encrypted_file, "r", encoding="utf-8") as f:
        encrypted_text = f.read()

    # Взлом шифра
    broken_text = caesar_break(encrypted_text)
    with open(broken_file, "w", encoding="utf-8") as f:
        f.write(broken_text)
    print(f"Восстановленный текст записан в файл: {broken_file}")


if __name__ == "__main__":
    test_caesar_break()
