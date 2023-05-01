import random
import statistics


def generate_password(pw_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pw_length:
        password = "".join(random.choices(alphabet, k=length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)

    return passwords


def replace_with_number(pword):
    replace_indices = random.sample(range(len(pword)), random.randrange(1, 3))
    for index in replace_indices:
        pword = pword[:index] + str(random.randrange(10)) + pword[index + 1:]

    return pword


def replace_with_uppercase_letter(pword):
    replace_indices = random.sample(range(len(pword) // 2, len(pword)), random.randrange(1, 3))
    for index in replace_indices:
        pword = pword[:index] + pword[index].upper() + pword[index + 1:]

    return pword


def main():
    num_values = int(input("How many values do you want to enter? "))
    print(f"Enter {num_values} values:")

    values = []
    for i in range(num_values):
        value = float(input(f"Value #{i + 1}: "))
        values.append(value)

    average = statistics.mean(values)

    print(f"The average of the entered values is: {average}")


if __name__ == "__main__":
    main()
