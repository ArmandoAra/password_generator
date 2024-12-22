
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_gen(nr_letters, nr_symbols, nr_numbers):
    password_letters = []
    password_symbols = []
    password_numbers = []

    counter_letters = 0
    counter_numbers = 0
    counter_symbols = 0

    letters_str = ""
    symbols_str = ""
    numbers_str = ""

    # loop de letras random
    for letters_repeat in range(0, nr_letters):
        counter_letters += 1
        a = random.randint(0, len(letters) - 1)
        password_letters.append(letters[a])
        letters_str += password_letters[counter_letters - 1]

    # loop de numeros
    for sy_repeat in range(0, nr_symbols):
        counter_symbols += 1
        b = random.randint(0, len(symbols) - 1)
        password_symbols.append(symbols[b])
        symbols_str += password_symbols[counter_symbols - 1]

    # loop de simbolos
    for nr_repeat in range(0, nr_numbers):
        counter_numbers += 1
        c = random.randint(0, len(numbers) - 1)
        password_numbers.append(numbers[c])
        numbers_str += password_numbers[counter_numbers - 1]

    password2 = letters_str + symbols_str + numbers_str

    new_password = []
    rep = 0
    new_pass_str = ""

    password = list(password2)

    nr_letras = len(password)

    for letra in range(0, len(password)):
        rep = random.randint(0, len(password) - 1)
        new_password.append(password[rep])
        password.pop(rep)

    count2 = 0

    for letra in range(0, len(new_password)):
        count2 += 1
        new_pass_str += new_password[count2 - 1]

    return new_pass_str
