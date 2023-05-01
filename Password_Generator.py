import random


def generate_password(lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    # Iterate over each length in the input list and generate a password with that length
    for length in lengths:

        # Generate a random password with the specified length
        password = "".join(random.choices(alphabet, k=int(length)))
        num_of_indices_for_numbers = random.randint(1, len(lengths))
        num_of_indices_for_uppercase = random.randint(1, len(lengths))

        # Choose the indices to replace with numbers and uppercase letters
        replace_indices_for_numbers = random.sample(range(int(length)), num_of_indices_for_numbers)
        replace_indices_for_uppercase = random.sample(range(int(length) // 2, int(length)), num_of_indices_for_uppercase)

        # Replace the chosen indices with numbers and uppercase letters
        for index in replace_indices_for_numbers:
            password = password[:index] + str(random.randrange(10)) + password[index + 1:]
        for index in replace_indices_for_uppercase:
            password = password[:index] + password[index].upper() + password[index + 1:]

        passwords.append(password)

    return passwords


def main():
    # Get the number of passwords to generate from the user
    num_values = int(input("How many passwords do you want to generate? "))
    lengths = []
    for i in range(num_values):
        length = int(input(f"Enter length of password #{i + 1}: "))
        lengths.append(length)

    # Generate the passwords and print them
    passwords = generate_password(lengths)
    print(f"Generated passwords: {passwords}")


if __name__ == "__main__":
    main()
