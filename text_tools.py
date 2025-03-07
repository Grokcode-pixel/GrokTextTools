# Grok’s Text Tools - Утилита для работы с текстом
import random
import string

def text_tools():
    print("Добро пожаловать в Grok’s Text Tools!")
    print("Выберите действие:")
    print("1. Перевод в ВЕРХНИЙ регистр")
    print("2. Перевод в нижний регистр")
    print("3. Сгенерировать случайный пароль")
    print("4. Подсчитать слова и символы")
    print("5. Очистить текст от лишних символов")
    
    choice = input("Введите номер действия (1-5): ")
    text = input("Введите текст: ")

    if choice == "1":
        result = text.upper()
        print(f"Результат: {result}")
    elif choice == "2":
        result = text.lower()
        print(f"Результат: {result}")
    elif choice == "3":
        length = int(input("Длина пароля (например, 12): "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Ваш пароль: {password}")
    elif choice == "4":
        words = len(text.split())
        chars = len(text)
        print(f"Слов: {words}, Символов: {chars}")
    elif choice == "5":
        result = ''.join(c for c in text if c.isalnum() or c.isspace())
        print(f"Очищенный текст: {result}")
    else:
        print("Неверный выбор, попробуйте снова!")

    print("\nПонравилось? Поддержите автора: https://boosty.to/grokcode/donate")

if __name__ == "__main__":
    text_tools()
